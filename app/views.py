from django.shortcuts import render
from django.http import JsonResponse
from .models import RSVP, Gift


def landing(request):
    ''' render html landing page '''
    render(request, 'landing.html', {})


def rsvp(request):
    ''' accept rsvp form submit via ajax '''
    # parse & validate form
    # save rsvp record to db
    # send sms confirmation
    # return json response
    return JsonResponse({})


def gift(request):
    ''' accept gift form submit via ajax '''
    # parse & validate form
    # make api request to stripe
    # handle api response
    # save gift record to db
    # send sms confirmation
    # return json response
    return JsonResponse({})

