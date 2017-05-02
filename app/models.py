from django.db.models import (
        Model, DateTimeField, CharField, IntegerField, TextField, EmailField
    )
from phonenumber_field.modelfields import PhoneNumberField


class RSVP(Model):
    timestamp = DateTimeField(auto_now_add=True)
    name = CharField(max_length=250)
    guests = IntegerField()
    note = TextField(null=False, blank=True)
    phone = PhoneNumberField()


class Gift(Model):
    timestamp = DateTimeField(auto_now_add=True)
    name = CharField(max_length=250)
    email = EmailField()
    order = CharField(max_length=250)   # stripe order id
    amount = IntegerField()             # stripe returns amounts as cents
    raw = TextField()                   # save the entire stripe response

