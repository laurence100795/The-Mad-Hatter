from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (  # displays valuables in admin view of specific products
        'name',
        'category',
        'price',
        'rating',
        'image',
        'sku',
    )

    ordering = ('name',)  # orders products in admin view


class CategoryAdmin(admin.ModelAdmin):
    list_display = (  # displays valuables in admin view of specific products
        'friendly_name',
        'name',
    )


# Registers products in admin view for management
admin.site.register(Product, ProductAdmin)
# Registers categories in admin view for management
admin.site.register(Category, CategoryAdmin)
