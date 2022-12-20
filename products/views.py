from django.shortcuts import render
from rest_framework import generics

from products.models import Products
from products.serializers import memberSerializers

# Create your views here.
class ProductView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = memberSerializers
