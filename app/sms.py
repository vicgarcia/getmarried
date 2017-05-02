from django.conf import settings
from plivo import RestAPI


def send_sms_message(number, message):
    ''' generic function to send sms message to number '''
    api = RestAPI(settings.PLIVO['id'], settings.PLIVO['token'])
    return api.send_message({
            'text': message,
            'src':  settings.PLIVO['src'],
            'dst':  number,
        })


def send_rsvp_confirmation(number):
    ''' function to send rsvp confirmation texts '''
    message = "Thanks for the RSVP. We can't wait to see you!"
    status, response = send_sms_message(number, message)
    # return True or False based on success

