
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import VolunteerProfile
from .forms import VolunteerProfileForm

# direct to login page if not logged in
@login_required
def volunteers(request):
    """ Display and update volunteer profile. """
    
    volunteer_profile = get_object_or_404(VolunteerProfile, user=request.user)
    if request.method == 'POST':
        form = VolunteerProfileForm(request.POST, instance=volunteer_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Volunteer profile updated successfully')
        else:
            messages.error(request, 'There was an error with your form')

    # GET request
    form = VolunteerProfileForm(instance=volunteer_profile)
    template = 'volunteers/volunteer.html'
    context = {
        'form': form,
    }
    return render(request, template, context)