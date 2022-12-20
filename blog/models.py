from django.db import models
from django.contrib import admin
from ckeditor.fields import RichTextField 

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=99)
    author = models.CharField(max_length=99)
    published_date = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=99)
    content = RichTextField()

    class Meta:
        verbose_name_plural = "Blog and Articles"  

class modelBlog(admin.ModelAdmin):
    list_display = ('title', 'author', 'category',)
    list_filter = ('title', 'author',)