import json
import stripe

from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import RSVP, Gift
from .forms import RSVPForm, GiftForm
from .sms import send_sms_message


IS_ATTENDING_MESSAGE = "Thanks for the RSVP! We can't wait to see you at our wedding. If you need anything you can reply to this text message to get in touch with us. \n- Gertie & Vic"

NOT_ATTENDING_MESSAGE = "Thank you for letting us know you won't be able to make it. We'll miss you on our special day. \n- Gertie & Vic"


def landing(request):
    ''' render html landing page '''
    return render(request, 'landing.html', {
            'stripe_public_key': settings.STRIPE['public_key'],
        })


def rsvp(request):
    ''' accept rsvp form submit via ajax '''
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            rsvp = form.save()
            if rsvp.attending:
                message = IS_ATTENDING_MESSAGE
            else:
                message = NOT_ATTENDING_MESSAGE
            send_sms_message(rsvp.phone, message)
            return JsonResponse({'success': True})
        else:
            messages = form.error_list()
            return JsonResponse({'success': False, 'messages': messages})
    return redirect('landing', permanent=True)


def _convert_amount_for_stripe(amount):
    ''' convert decimal value from form to int for stripe '''
    return int( str(amount).replace('.', '') )


def gift(request):
    ''' accept gift form submit via ajax '''
    if request.method == 'POST':
        form = GiftForm(request.POST)
        errors = []
        if form.is_valid():
            gift = form.save()
            stripe.api_key = settings.STRIPE['private_key']
            try:
                charge = stripe.Charge.create(
                    amount=_convert_amount_for_stripe(gift.amount),
                    currency='usd',
                    source=request.POST['token'],
                    description='wedding gift from {}'.format(gift.email),
                    receipt_email=gift.email,
                )
                gift.raw = json.dumps(charge)
                gift.save()
                return JsonResponse({'success': True})
            except stripe.error.CardError as e:
                errors.append(e.json_body['error']['message'])
            except Exception:
                errors.append('An unknown error occurred.')
        else:
            errors.extend(form.error_list())
        return JsonResponse({'success': False, 'messages': errors})
    return redirect('landing', permanent=True)


@csrf_exempt
def sms(request):
    ''' accept an incoming sms message and forward it to me & gertie '''
    if request.method == 'POST':
        try:
            text = request.POST['Text']
            source = request.POST['From'][1:]
        except KeyError:
            return HttpResponse(status=400)
        try:
            sender = RSVP.objects.get(phone=source).name
        except (RSVP.DoesNotExist, RSVP.MultipleObjectsReturned):
            sender = 'none'
        message = '{}\n-{} <{}>'.format(text, sender, source)
        for number in settings.PLIVO['relay']:
            send_sms_message(number, message)
        return HttpResponse(status=200)
    return redirect('landing', permanent=True)

