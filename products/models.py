from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid


class Category(models.Model):

    class Meta:
        # Changes admin view name of Categorys to Categories
        verbose_name_plural = 'Categories'
        # orders categories by there names
        ordering = ('name',)

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=50, blank=True, unique=True,
                           default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=35)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(validators=[MinValueValidator(0),
                                 MaxValueValidator(5)],
                                 max_digits=3, decimal_places=2,
                                 null=True, blank=True)
    image_url = models.URLField(max_length=1024, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
