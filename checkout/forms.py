from django import forms
from .models import Order
from django.core.exceptions import ValidationError



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County',
            'postcode': 'Post Code. CF31 or CF34 only please',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border border-primary rounded-0 mt-2 shadow-none'
            self.fields[field].label = False


    def clean_postcode(self):
        data = self.cleaned_data["postcode"]
        # check for valid postcode
        if "CF34" not in data and "CF31" not in data and "cf34" not in data and "cf31" not in data:
            raise ValidationError("Invalid postcode")
        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data
