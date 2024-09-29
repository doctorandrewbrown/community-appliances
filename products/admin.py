from django.contrib import admin
from .models import Product, Category, Condition, Certificate

# the classes below extend the admin model to tell admin view what data to show


class CertificateAdmin(admin.ModelAdmin):
    # tuple below note () brackets
    list_display = (
        'certificate',
    )


class ProductAdmin(admin.ModelAdmin):
    # tuple below note () brackets
    list_display = (
        'name',
        'category',
        'grade',
        'price',
        'image'
    )
# chose option to order admin view note tuple
    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class ConditionAdmin(admin.ModelAdmin):
    list_display = ('grade', 'description')
    ordering = ('grade',)

# Register your models here. Note admin models defined above are registered
# alongside respective models


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Condition, ConditionAdmin)
admin.site.register(Certificate, CertificateAdmin)
