from django.contrib import admin

# Register your models here.
import apps.IntegratedFood

admin.site.register(apps.IntegratedFood.models.StepProduction)
admin.site.register(apps.IntegratedFood.models.BromotaologicFactSheetIF)
admin.site.register(apps.IntegratedFood.models.IngredientIF)
admin.site.register(apps.IntegratedFood.models.ProfileMediterraneanDiet)
admin.site.register(apps.IntegratedFood.models.FoodIntegrated)
admin.site.register(apps.IntegratedFood.models.collegamento_integredfood_IngredientIF)
