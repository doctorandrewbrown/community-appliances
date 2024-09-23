
from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404, HttpResponse)
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from profiles.forms import UserProfileForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
from cart.contexts import cart_contents

from django.core.mail import send_mail

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        # get user input form data
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county']}
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            # save order info to order model
            order = order_form.save()
            for item_id, item_data in cart.items():
                product = Product.objects.get(id=item_id)
                if isinstance(item_data, int):
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                        )
                    # save to order_line_item model
                    order_line_item.save()

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                           'checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Did you enter a valid CF34 or CF31 postcode?')
            return redirect(reverse('checkout'))
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.info(request, 'There are no items in \
                your cart to checkout')
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Attempt to prefill the form from users profile
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.default_full_name,
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()
        if not stripe_public_key:
            messages.error(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,

        }

        return render(request, template, context)


def checkout_success(request, order_number):
    """
        Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_full_name': order.full_name,
                'default_phone_number': order.phone_number,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data,
                                                instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    if 'cart' in request.session:
        # empty cart
        del request.session['cart']
    send_mail(
    "Subject here",
    "Checkout Success!",
    "communityapplianceswales@gmail.com",
    ["dr.andrew.david.brown@gmail.com"],
    fail_silently=False,)

    messages.success(request, 'Checkout succcessful! Your order will \
                     be delivered within five working days.')
    template = 'checkout/checkout_success.html'
    context = {'order': order, }
    return render(request, template, context)



