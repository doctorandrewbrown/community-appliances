from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your bag is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form, 'stripe_public_key': 'pk_test_51PEsYP01b0caL7kaca7zrnbpbcgs0xhGoM1dF9VBWLr1CWtKCG0m5K2Mq9JXpkp6qh2akURWlEc01NAHKArotVeX00fQFLZ0v9',
        'client_secret': 'test client secret',

    }

    return render(request, template, context)