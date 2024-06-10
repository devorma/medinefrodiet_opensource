from django.contrib import admin

# Register your models here.

from .models import Patient, MeelRecord
admin.site.register(Patient)
admin.site.register(MeelRecord)