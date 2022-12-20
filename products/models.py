import uuid
from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model


# Create your models here.
SIZE_CHOICES = (
    ('XXS', 'XXS'),
    ('XS', 'XS'),
    ('XS-S', 'XS-S'),
    ('S', 'S'),
    ('M', 'M'),
    ('M-L', 'M-L'),
    ('L', 'L'),
    ('XL', 'XL'),
)

RATINGS = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5")
)

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    product_category = models.CharField(max_length=90)

    def __str__(self):
        return str(self.product_category)

    class Meta:
        verbose_name_plural = "Categories"  


class modelCategory(admin.ModelAdmin):
    list_display = ('product_category',)
    list_filter = ('product_category',)

class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    product_name = models.CharField(max_length=90, unique=True)
    product_price = models.IntegerField()
    product_category = models.ForeignKey(Category, max_length=90, on_delete=models.PROTECT)
    product_sub_category = models.CharField(max_length=90)
    product_description = models.TextField(null=True, blank=True)
    product_color = models.CharField(max_length=90, null=True, blank=True)
    product_size = models.CharField(max_length=90, choices=SIZE_CHOICES, null=True, blank=True)
    product_rating = models.CharField(max_length=90, choices=RATINGS)
    is_inOffer = models.BooleanField(default=False, verbose_name="In Offer")
    images = models.FileField(upload_to='images/', null=True, blank=True, verbose_name='Images')
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    is_inStock = models.BooleanField(default=True, verbose_name="In Stock")
    is_active = models.BooleanField(default=True, verbose_name="Is the product active?")


    class Meta:
        verbose_name_plural = "Items"

class modelProducts(admin.ModelAdmin):
    list_display = ('product_name', 'product_price', 'product_category', 'is_inOffer', 'is_inStock',)
    list_filter = ('product_name', 'product_price', 'product_category', 'is_inStock', 'is_inOffer')
    list_editable = ('is_inStock', )

    
