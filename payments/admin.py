from django.contrib import admin

from payments.models import BillingInfo, modelBillingInfo

# Register your models here.
admin.site.register(BillingInfo, modelBillingInfo)