from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.


def all_products(request):
    """ A view to show all products and sorted products"""
    # get all products from database
    products = Product.objects.all()
    # set value for category to pass in context where no category is passed in GET request
    category = 'All Appliances'
    # check query for category and sort conditions
    if request.GET:
        # sort by price or grade
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            # sort by high to low price
            if sortkey == 'price':
                print("price")
                products = products.order_by("-" + sortkey)
            # or sort by condition A to C
            elif sortkey == 'grade':
                products = products.order_by(sortkey)
            else: products = products.order_by('-price')

        # filter sorted products by category
        if 'category' in request.GET:
            category = request.GET['category'].split(',')
            products = products.filter(category__name__in=category)
            # get category to pass to template
            category = category[0]
            # if invalid category in query
            if len(products) == 0: category = "no appliances found"
        else:
            products = products.order_by('-price')

    # if no query set in GET request show all products with descending price
    else: 
        products = products.order_by('-price')

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
