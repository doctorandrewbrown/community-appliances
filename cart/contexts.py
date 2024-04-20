
from decimal import Decimal
from django.conf import settings


def cart_contents(request):
    cart_items = []
    total = 0
    product_count = 0


    if total > settings.DISCOUNT_THRESHOLD:
        discount = total * Decimal(settings.PERCENTAGE_DISCOUNT / 100)
        
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
