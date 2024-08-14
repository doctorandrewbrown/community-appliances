from django.contrib import admin

# Register your models here.
from .models import UserProfile



class UserProfileAdmin(admin.ModelAdmin):

    fields = (
            'default_full_name',
            'default_phone_number',
            'default_street_address1',
            'default_street_address2',
            'default_town_or_city',
            'default_county',
            'default_postcode',
            #'default_country',
            )

admin.site.register(UserProfile, UserProfileAdmin)
