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

