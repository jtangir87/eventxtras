from django.contrib import admin
from .models import Category, CategoryFilter, Product, ProductImage


# Register your models here.
admin.site.register(Category)
admin.site.register(CategoryFilter)
admin.site.register(Product)
admin.site.register(ProductImage)
