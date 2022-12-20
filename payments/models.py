from django.db import models
from django.contrib import admin
# Create your models here.

class BillingInfo(models.Model):
    first_name = models.CharField(max_length=99, editable=False)
    middle_name = models.CharField(max_length=99, editable=False, blank=True, null=True)
    last_name = models.CharField(max_length=99, editable=False)
    phone_number = models.CharField(max_length=99, editable=False)
    email_address = models.EmailField(max_length=99, editable=False, blank=True, null=True)
    amount = models.IntegerField(editable=False)
    currency = models.CharField(max_length=3, editable=False)
    description = models.TextField(max_length=200, editable=False)
    country_code = models.CharField(max_length=3, editable=False, blank=True, null=True)
    zip_code = models.CharField(max_length=99, editable=False, blank=True, null=True)
    notification_id = models.CharField(max_length=99, editable=False, blank=True, null=True)
    payment_status = models.BooleanField(default=False, editable=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Customer Billing Info"  

class modelBillingInfo(admin.ModelAdmin):
    list_display = ('first_name', 'phone_number', 'email_address', 'payment_status',)
    list_filter = ('first_name', 'phone_number', 'email_address', 'amount', 'notification_id',)

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': False,
            'show_save_and_continue': False,
            'show_delete': False,
            'show_save_and_add_another': False
        })
        return super().render_change_form(request, context, add, change, form_url, obj)