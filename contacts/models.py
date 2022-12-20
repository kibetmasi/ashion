from django.db import models
from django.contrib import admin

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=99, editable=False)
    email = models.EmailField(editable=False)
    phone_number = models.CharField(max_length=99, editable=False)
    website = models.CharField(max_length=99, editable=False)
    subject = models.CharField(max_length=99, editable=False)
    message = models.TextField(max_length=300, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Messages"  

class modelContacts(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject',)
    list_filter = ('name', 'email', 'phone_number')

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': False,
            'show_save_and_continue': False,
            'show_delete': False,
            'show_save_and_add_another': False
        })
        return super().render_change_form(request, context, add, change, form_url, obj)