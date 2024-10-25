from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Category
from django.contrib import messages
from .forms import ProductForm
# Create your views here.


def all_products(request):
    """ A view to show all products and sorted products"""

    # get all products from database
    products = Product.objects.all()

    # set value for category to pass in context where
    # no category is passed in GET request
    category = 'All Appliances'

    # check query for category and sort conditions
    if request.GET:
        # filter sorted products by category
        if 'category' in request.GET:
            category = request.GET['category'].split(',')
            products = products.filter(category__name__in=category)

            # get category to pass to template
            category = category[0]
            # if invalid category in query or no products found
            if len(products) == 0:
                category = "no appliances found"

        # sort by price or grade
        if 'sort' in request.GET:
            sortkey = request.GET['sort']

            # sort by high to low price
            if sortkey == 'price_descending':
                products = products.order_by("-price")

            # sort by low to high price
            elif sortkey == 'price_ascending':
                products = products.order_by("price")

            # or sort by condition A to C
            elif sortkey == 'grade_ascending':
                products = products.order_by("grade")

            # or sort by condition C to A
            elif sortkey == 'grade_descending':
                products = products.order_by("-grade")

            # default ordering for no valid sortkey in query
            else:
                products = products.order_by('-price')

        # default ordering if "sort" not in query
        else:
            products = products.order_by('-price')

    # if no query parameters in GET request show
    # all products with descending price
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

def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)