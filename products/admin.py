from django.contrib import admin
from .models import Product, Category

# the two classes below extend the admin model to tell admin view what data to show


class ProductAdmin(admin.ModelAdmin):
    # tuple below
    list_display = (
        'name',
        'category',
        'description',
        'price',
        'image',
    )
# chose option to order admin view note tuple
    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

# Register your models here. Note admin models defined above are registered 
# alongside respective models


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)