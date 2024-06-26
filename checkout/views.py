
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from cart.contexts import cart_contents

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
            'country': request.POST['country'],
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
            return redirect(reverse('checkout_success'))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
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