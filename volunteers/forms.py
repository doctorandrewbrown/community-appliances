from django import forms
from .models import VolunteerProfile


class VolunteerProfileForm(forms.ModelForm):
    class Meta:
        model = VolunteerProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'volunteer_full_name': 'Full Name',
        }

        self.fields['volunteer_full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border border-dark rounded-0 mt-3'
            self.fields[field].label = False