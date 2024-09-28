
# Register your models here.
from django.contrib import admin
from .models import VolunteerProfile


class VolunteerAdmin(admin.ModelAdmin):

    fields = ('volunteer_full_name', 'details', 'active',)
    
    # show volunteer active status in admin change list display 
    list_display = ('user', 'active')


admin.site.register(VolunteerProfile, VolunteerAdmin)
