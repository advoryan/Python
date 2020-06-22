from django.contrib import admin
from . models import *

class ReportAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Report._meta.get_fields()]

    class Meta:
        model = Report

admin.site.register(Report, ReportAdmin)