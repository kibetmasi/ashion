from django.contrib import admin

from products.models import Category, Products, modelCategory, modelProducts

# Register your models here.
admin.site.register(Products, modelProducts)
admin.site.register(Category, modelCategory)