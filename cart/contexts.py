
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})
    # .items is a dict method
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product,
        })

    # Calculate discount
    if total > settings.DISCOUNT_THRESHOLD:
        discount = total * Decimal(settings.PERCENTAGE_DISCOUNT / 100)
        discount_delta = 0
    else: 
        discount = 0
        discount_delta = settings.DISCOUNT_THRESHOLD - total
    
    grand_total = total - discount

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'discount': discount,
        'discount_delta': discount_delta,
        'percentage_discount': settings.PERCENTAGE_DISCOUNT,
        'discount_threshold': settings.DISCOUNT_THRESHOLD,
        'grand_total': grand_total
    }

    return context
