from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.core.exceptions import PermissionDenied

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order

# direct to login page if not logged in
@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect(reverse('profile'))
        else:
            messages.error(request, 'There was a problem with your form. Did you enter a valid CF34 or CF31 postcode?')
            return redirect(reverse('profile'))

    form = UserProfileForm(instance=profile)
    # order by descending date
    orders = profile.orders.all().order_by('-date')
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """ Display order history """

    # get order using order number in get request 
    order = get_object_or_404(Order, order_number=order_number)

    # get order owner username for requested order from Order model
    order_owner = order.user_profile.user.username

    # get username for current logged in user
    current_user = get_object_or_404(UserProfile, user=request.user).user.username
    
    # check the logged-in user owns the order or trigger 403.html page
    if current_user != order_owner:
        raise PermissionDenied() 

    messages.info(request, (
        f'These are details of a previous order number {order_number}. '
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
        }

    return render(request, template, context)