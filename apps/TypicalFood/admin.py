from django.contrib import admin

# Register your models here.
from .models import GeographicalArea, BromotaologicFactSheet, TypicalityProfile, TypicalFood
admin.site.register(GeographicalArea)
admin.site.register(BromotaologicFactSheet)
admin.site.register(TypicalityProfile)
admin.site.register(TypicalFood)