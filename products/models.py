from django.db import models


# Create your models here.
class Certificate(models.Model):
    """
    A Certificate model for maintaining details of appliance safety
    certificates
    """
    certificate = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)

    # string representation of model
    def __str__(self):
        return self.certificate


class Condition(models.Model):
    """
    A  model for maintaining details of appliance condition A-C
    """
    class Meta:
        verbose_name_plural = "Condition"
    grade = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)

    # string representations of model
    def __str__(self):
        return self.grade


class Category(models.Model):
    """
    A Category model for maintaining
    details of appliance categories
    """

    # corrects plural in admin view
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)

    # string representations of model
    def __str__(self):
        return self.name


class Product(models.Model):
    """
    A Product model for maintaining appliance details
    """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True,)
    grade = models.ForeignKey('Condition', null=True, blank=True,
                              on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    certificate = models.ForeignKey('Certificate', null=True, blank=True,
                                    on_delete=models.SET_NULL)
    image = models.ImageField()

    # string representations of model
    def __str__(self):
        return self.name
