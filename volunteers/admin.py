
# Register your models here.
from django.contrib import admin
from .models import VolunteerProfile


class VolunteerAdmin(admin.ModelAdmin):

    fields = ('volunteer_full_name', 'email', 'details',)


admin.site.register(VolunteerProfile, VolunteerAdmin)
