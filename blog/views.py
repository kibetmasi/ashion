from django.shortcuts import render
from rest_framework import generics

from blog.models import Blog
from blog.serializers import BlogSerializers

# Create your views here.
class BlogView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
