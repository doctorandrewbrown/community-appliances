from django.db import models


# Create your models here.
class Certificate(models.Model):
    certificate = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)

    # string representation of model
    def __str__(self):
        return self.certificate


class Condition(models.Model):
    class Meta:
        verbose_name_plural = "Condition"
    grade = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    # string representations of model
    def __str__(self):
        return self.grade

    def get_friendly_name(self):
        return self.friendly_name


class Category(models.Model):

    # corrects plural in admin view
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    # string representations of model
    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    grade = models.ForeignKey('Condition', null=True, blank=True,
                              on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    certificate = models.ForeignKey('Certificate', null=True, blank=True,
                                    on_delete=models.SET_NULL)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    # string representations of model
    def __str__(self):
        return self.name
