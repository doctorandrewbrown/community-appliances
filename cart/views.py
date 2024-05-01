from django.shortcuts import render, redirect


# Create your views here.


def view_cart(request):
    """ A view for users to see cart contents """

    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    """ A view to add product to cart """

    # look for cart in session if it already
    # exists else create empty session dict
    cart = request.session.get('cart', {})
    # update cart contents in session dict
    request.session['cart'] = cart
    # add a product quantity of 1 to provide a key:value pair in session dict.
    # This will also overwrite an
    # existing id so same product can not be bought twice if attempted
    cart[product_id] = 1
    # redirect to current page (ie product details) when add to bag complete
    redirect_url = request.POST.get('redirect_url')
    return redirect(redirect_url)


def remove_from_cart(request, product_id):
    """ A view to remove product from cart """
    # get cart fom session or create
    cart = request.session.get('cart', {})
    # pop product from cart
    cart.pop(product_id)
    # update session dict
    request.session['cart'] = cart
    # return user to updated cart
    redirect_url = request.POST.get('redirect_url')
    return redirect(redirect_url)
