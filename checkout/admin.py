from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('product', 'lineitem_total', 'order', 'quantity',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'discount', 'order_total',
                       'grand_total',)

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county',
              'order_total', 'discount', 'grand_total',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'discount',
                    'grand_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
