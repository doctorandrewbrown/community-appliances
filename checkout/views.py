from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings


from .forms import OrderForm
from cart.contexts import cart_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],}
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            #order = order_form.save(commit=False)
            #pid = request.POST.get('client_secret').split('_secret')[0]
            #order.stripe_pid = pid
            #order.original_bag = json.dumps(bag)
            order_form.save()
        return redirect(reverse('checkout_success'))
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Your cart is empty")
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        
        order_form = OrderForm()
        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form, 
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,

        }
        
        return render(request, template, context)

def checkout_success(request):
    """
        Handle successful checkouts
    """

    if 'cart' in request.session:
        del request.session['cart']

        template = 'checkout/checkout_success.html'

    return render(request, template)