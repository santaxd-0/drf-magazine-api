from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name="Category name", blank=False, max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Item(models.Model):
    name = models.CharField(verbose_name="Item name", max_length=50, blank=False)
    slug = models.SlugField(verbose_name="Item slug", max_length=120, blank=False)
    price = models.DecimalField(verbose_name="Item cost", blank=False, decimal_places=2, max_digits=10)
    discount = models.DecimalField(verbose_name="Item discount", blank=False, default=0, decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"