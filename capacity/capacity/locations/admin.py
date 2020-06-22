from django.contrib import admin
from . models import *

class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']  # указанные поля
    
    class Meta:
        model = Location

admin.site.register(Location, LocationAdmin)
