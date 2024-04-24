from django.shortcuts import render, redirect


# Create your views here.


def view_cart(request):
    """ A view for users to see cart contents """

    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    """ A view to add product to cart """
    # redirect to current page ie product details
    redirect_url = request.POST.get('redirect_url')

    # look for cart in session if it already exists else create it
    cart = request.session.get('cart', {})
    request.session['cart'] = cart
    cart[product_id] = 1
    # print(request.session['cart'])
    return redirect(redirect_url)
    