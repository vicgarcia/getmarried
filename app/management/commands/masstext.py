from django.core.management.base import BaseCommand, CommandError
from app.models import RSVP
from app.sms import send_sms_message



class Command(BaseCommand):
    help = 'Mass text to guests who are attending.'

    def add_arguments(self, parser):
	pass

    def handle(self, *args, **options):
	for rsvp in RSVP.objects.filter(attending=True):
	    resp = send_sms_message(rsvp.phone, message)

