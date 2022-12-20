from django.contrib import admin

from blog.models import Blog, modelBlog

# Register your models here.
admin.site.register(Blog, modelBlog)