from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings


from .forms import OrderForm
from cart.contexts import cart_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
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
        'stripe_public_key': 'pk_test_51PEsYP01b0caL7kaca7zrnbpbcgs0xhGoM1dF9VBWLr1CWtKCG0m5K2Mq9JXpkp6qh2akURWlEc01NAHKArotVeX00fQFLZ0v9',
        'client_secret': 'test client secret',

    }
    #messages.success(request, 'Order successfully processed!')
    return render(request, template, context)

def checkout_success(request, order_number):
        """
            Handle successful checkouts
        """

        if 'cart' in request.session:
            del request.session['cart']

            template = 'checkout/checkout_success.html'

            return render(request, template)