from django import forms
from .models import VolunteerProfile


class VolunteerProfileForm(forms.ModelForm):
    class Meta:
        model = VolunteerProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, remove auto-generated
        labels and set autofocus for non-checkbox fields. Add bootstrap classes
        """
        super().__init__(*args, **kwargs)
        # form placeholders for fields other than checkbox
        placeholders = {
            'volunteer_full_name': 'Full Name',
            'details': 'about you'
        }

        self.fields[
                   'volunteer_full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            # if field is not checkbox
            if field != 'active':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                # add bootstrap classes
                self.fields[field].widget.attrs['class'] = 'border \
                    border-primary shadow-none rounded-0 mt-3'
                # remove auto generated field labels
                self.fields[field].label = False
            else:
                # add bootstrap classes to checkbox
                self.fields[field].widget.attrs['class'] = 'border \
                    border-primary shadow-none rounded-0'
