from django import forms
from .models import RSVP, Gift
import re


class RSVPForm(forms.ModelForm):

    class Meta:
        model = RSVP
        fields = [ 'name', 'attending', 'guests', 'phone', 'note' ]

    name = forms.CharField(
            error_messages={
                'required': 'Please provide your name.',
                'max_length': 'Please limit name to 250 characters.',
            }
        )

    phone = forms.CharField(
            max_length=None,
            error_messages={
                'required': 'Please provide a phone number.',
            }
        )

    guests = forms.IntegerField(
            required=False,
            error_messages={
                'invalid': 'Please provide a number of guests.',
            }
        )

    def clean_guests(self):
        ''' ensure a null value for guests is set to 0 '''

        data = self.cleaned_data['guests']
        if not data:
            data = 0

        return data

    def clean_phone(self):
        ''' clean the phone number input to a 10 digit string '''

        # parse out common phone symbols
        data = self.cleaned_data['phone']
        data = re.sub(r'\.|\+|\(|\)|\-|\ ', '', data)

        # if the phone number starts w/ 1, remove it
        if data[0] == '1':
            data = data[1:]

        # check that phone value contains 10 digits
        if not data.isdigit() or len(data) != 10:
            raise forms.ValidationError('Please provide a valid phone number.')

        # return the cleaned phone number
        return data

    def error_list(self):
        ''' return a flat list of errors for use in ajax form '''

        # the order of fields controls order of messages in error list
        error_order = [ 'name', 'guests', 'phone' ]

        # work through the form model components to get error message strings
        error_data = self.errors.as_data()
        error_list = []
        for field in error_order:
            if field in error_data:
                for error in error_data[field]:
                    error_list.append(error.message)

        # return a flat list of error strings
        return error_list


class GiftForm(forms.ModelForm):

    class Meta:
        model = Gift
        fields = [ 'name', 'email', 'note', 'amount' ]

    name = forms.CharField(
            error_messages={
                'max_length': 'Please limit name to 250 characters.',
                'required': 'Please provide your name.',
            }
        )

    email = forms.EmailField(
            error_messages={
                'max_length': 'Please limit email address to 250 characters.',
                'required': 'Please provide your email address.',
                'invalid': 'Please provide a valid email address.',
            }
        )

    amount = forms.DecimalField(
            max_value=1000.00,
            min_value=10.00,
            error_messages={
                'min_value': 'Please provide an amount over $10.',
                'max_value': 'Please provide an amount below $1000.',
                'max_decimal_places': 'Please specify gift amount with 2 decimal places.',
                'required': 'Please provide a gift amount.',
                'invalid': 'Please provide a valid gift amount.',
            }
        )

    def error_list(self):
        ''' return a flat list of errors for use in ajax form '''

        # the order of fields controls order of messages in error list
        error_order = [ 'name', 'email', 'amount' ]

        # work through the form model components to get error message strings
        error_data = self.errors.as_data()
        error_list = []
        for field in error_order:
            if field in error_data:
                for error in error_data[field]:
                    error_list.append(error.message)

        # return a flat list of error strings
        return error_list

    def save(self):
        ''' override save method to default to commit=False '''
        return super(GiftForm, self).save(commit=False)

