from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.


def all_products(request):
    """ A view to show all products and sorted products"""
    products = Product.objects.all()
    # set value for category where no category is passed in GET request
    category = 'All Appliances'
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            # sort by descending price
            if sortkey == 'price':
                products = products.order_by("-" + sortkey)
            else:
                products = products.order_by(sortkey)

        if 'category' in request.GET:
            category = request.GET['category'].split(',')
            products = products.filter(category__name__in=category)
            # get category from request object to pass to UI
            category = category[0]

    context = {
        'products': products,
        'category': category
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
