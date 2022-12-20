from django.contrib import admin

from contacts.models import Contacts, modelContacts

# Register your models here.
admin.site.register(Contacts, modelContacts)