from django.contrib import admin
from .models import *


class EshopAdmin(admin.ModelAdmin):
    list_display = ('Productname','price','Quantity')



admin.site.register(E_Shop,EshopAdmin)