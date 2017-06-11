import json

from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, JsonResponse

from .models import RSVP, Gift
from .forms import RSVPForm, GiftForm
from .sms import send_rsvp_confirmation



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
            send_rsvp_confirmation(rsvp.phone)
            return JsonResponse({'success': True})
        else:
            messages = form.error_list()
            return JsonResponse({'success': False, 'messages': messages})
    return redirect('landing', permanent=True)


def gift(request):
    ''' accept gift form submit via ajax '''
    # parse & validate form
    # make api request to stripe
    # handle api response
    # save gift record to db
    # send sms confirmation
    # return json response
    return JsonResponse({})


def sms(request):
    ''' handle incoming sms postback from plivo '''
    sender = request.POST['From']
    message = request.POST['Text']
    # resend the message to us
    return HttpResponse('Message received', status=200)

