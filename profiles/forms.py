from django import forms
from .models import UserProfile
from django.core.exceptions import ValidationError


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Full Name',
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_county': 'County',
            'default_postcode': 'Post Code. CF31 or CF34 only please',
        }

        self.fields['default_full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border border-primary shadow-none rounded-0 mt-3'
            self.fields[field].label = False

   
    def clean_default_postcode(self):
        """
        Check for valid default postcode 
        """
        data = self.cleaned_data["default_postcode"]
        # check for valid postcode
        if "CF34" not in data and "CF31" not in data and "cf34" not in data and "cf31" not in data:
            raise ValidationError("Invalid postcode")
        return data