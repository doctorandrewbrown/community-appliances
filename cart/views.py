from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


def view_cart(request):
    """ A view for users to see cart contents """
    # check if cart is empty
    cart = request.session.get('cart', {})
    if len(cart) == 0:
        messages.warning(request, 'Your cart is empty')

    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    """ A view to add product to cart """

    # look for cart in session if it already
    # exists else create empty session dict
    cart = request.session.get('cart', {})
    # update cart contents in session dict
    request.session['cart'] = cart
    # check if item is already in cart.
    if product_id in cart:
        # flash message
        messages.warning(request, 'The item is already in your cart!')
        # redirect to current page (ie product details) if item already in cart.
        redirect_url = request.POST.get('redirect_url')
        return redirect(redirect_url)
    else:
        # add item to cart
        cart[product_id] = 1
        # flash message
        messages.success(request, 'The item has been added to your cart')
        # redirect to current page (ie product details) when add to cart complete
        redirect_url = request.POST.get('redirect_url')
        return redirect(redirect_url)


def remove_from_cart(request, product_id):
    """ A view to remove product from cart """
    # flash message to user
    messages.warning(request, 'The item has been removed from your cart')
    # get cart fom session or create
    cart = request.session.get('cart', {})
    # pop product from cart
    cart.pop(product_id)
    # update session dict
    request.session['cart'] = cart
    # return user to updated cart
    redirect_url = request.POST.get('redirect_url')
    return redirect(redirect_url)
