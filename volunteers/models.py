
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class VolunteerProfile(models.Model):
    """
    A volunteer profile model for maintaining volunteer details
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    volunteer_full_name = models.CharField(max_length=80, null=False, blank=False)
    email = models.EmailField(max_length=80, null=False, blank=False, default='@')
    details = models.TextField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_volunteer_profile(sender, instance, created, **kwargs):
    """
    Create or update the volunteer profile
    """
    #if created:
    VolunteerProfile.objects.create(user=instance)
    #Existing users: just save the profile
    #instance.volunteerprofile.save()