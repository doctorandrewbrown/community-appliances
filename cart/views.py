from django.shortcuts import render


# Create your views here.


def view_cart(request):
    """ A view for users to see cart contents """

    return render(request, 'cart/cart.html')