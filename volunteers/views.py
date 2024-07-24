
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib import messages


def volunteers(request):
    """ Display volunteer profile. """
   
    template = 'volunteers/volunteer.html'

    return render(request, template)