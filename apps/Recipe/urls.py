from neapolitan.views import CRUDView
from django.urls import path
import apps.Recipe
from . import views
class collegamento_recipeintegred_bromotaologicfactsheetView(CRUDView):
    model = apps.Recipe.models.collegamento_recipeintegred_bromotaologicfactsheet
    fields = ["bromotaologicfactsheet", "recipe"]

class DirectionsProcessProductionView(CRUDView):
    model = apps.Recipe.models.DirectionsProcessProduction
    fields = ["ingredient", "directions"]

class BromotaologicFactSheetRView(CRUDView):
    model = apps.Recipe.models.BromotaologicFactSheetR
    fields = ["name", "kcal","proteins","fats",'carbs','peso_in_grammi']

class MerciologicalIndicationsView(CRUDView):
    model = apps.Recipe.models.MerciologicalIndications
    fields = ["indications"]

class PalatabilitySheetView(CRUDView):
    model = apps.Recipe.models.PalatabilitySheet
    fields = ["taste","texture"]

class RecipeIntegratedMediterraneanFoodView(CRUDView):
    model = apps.Recipe.models.RecipeIntegratedMediterraneanFood
    fields = ["name","carbs","proteins","fats"]

class collegamento_recipe_integredfoodView(CRUDView):
    model = apps.Recipe.models.collegamento_recipe_integredfood
    fields = ["food_integrated","recipe"]


urlpatterns = collegamento_recipeintegred_bromotaologicfactsheetView.get_urls() + DirectionsProcessProductionView.get_urls() + BromotaologicFactSheetRView.get_urls() + MerciologicalIndicationsView.get_urls() + PalatabilitySheetView.get_urls() + RecipeIntegratedMediterraneanFoodView.get_urls() + collegamento_recipe_integredfoodView.get_urls() +[
    path("Recipe_detail.html", views.crearicetta, name='Recipe-detail'),
    path("Recipe.html", views.consultaricetta, name='Recipe-Home'),
    path("Recipe_info.html", views.dettaglio_ricetta, name='Recipe-Info'),

]