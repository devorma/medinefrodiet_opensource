from django.contrib import admin

# Register your models here.
import apps.Recipe

admin.site.register(apps.Recipe.models.DirectionsProcessProduction)
admin.site.register(apps.Recipe.models.BromotaologicFactSheetR)
admin.site.register(apps.Recipe.models.collegamento_recipeintegred_bromotaologicfactsheet)
admin.site.register(apps.Recipe.models.MerciologicalIndications)
admin.site.register(apps.Recipe.models.PalatabilitySheet)
admin.site.register(apps.Recipe.models.RecipeIntegratedMediterraneanFood)
admin.site.register(apps.Recipe.models.collegamento_recipe_integredfood)