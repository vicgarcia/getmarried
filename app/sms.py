from django.conf import settings
from plivo import RestAPI


def send_sms_message(number, message):
    ''' generic function to send sms message to number '''
    api = RestAPI(settings.PLIVO['id'], settings.PLIVO['token'])
    return api.send_message({
            'text': message,
            'src':  settings.PLIVO['src'],
            'dst':  '1' + number,
        })


def send_rsvp_confirmation(number):
    ''' function to send rsvp confirmation texts '''
    message = "Thanks for the RSVP! We can't wait to see you at our wedding. If you need anything you can reply to this text message to get in touch with us. \n- Gertie & Vic"
    status, response = send_sms_message(number, message)
    return status == 202

