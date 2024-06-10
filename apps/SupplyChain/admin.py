from django.contrib import admin

# Register your models here.
import apps.SupplyChain

admin.site.register(apps.SupplyChain.models.SupplyChain)
admin.site.register(apps.SupplyChain.models.FactorsSelectionSupplyChain)
admin.site.register(apps.SupplyChain.models.BromotaologicFactSheetSC)
admin.site.register(apps.SupplyChain.models.SheetNecessityPreprocessing)
admin.site.register(apps.SupplyChain.models.FoodFromTheSupplyChain)