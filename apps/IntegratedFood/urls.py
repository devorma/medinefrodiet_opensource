from neapolitan.views import CRUDView

import apps.IntegratedFood

class FoodIntegratedView(CRUDView):
    model = apps.IntegratedFood.models.FoodIntegrated
    fields = ["name", "ingredient", "profile_mediterranean_diet","price","expiry_date"]

class ProfileMediterraneanDietView(CRUDView):
    model = apps.IntegratedFood.models.ProfileMediterraneanDiet
    fields = ["name", "description"]

class IngredientIFView(CRUDView):
    model = apps.IntegratedFood.models.IngredientIF
    fields = ["name", "step_production","bromotaologic_fact_sheet"]


class BromotaologicFactSheetIFView(CRUDView):
    model = apps.IntegratedFood.models.BromotaologicFactSheetIF
    fields = ["name", "calories_per_serving","proteins","fats","carbohydrates","vitamins","minerals","allergens"]

class StepProductionView(CRUDView):
    model = apps.IntegratedFood.models.StepProduction
    fields = ["name", "description"]

class collegamento_integredfood_IngredientIFView(CRUDView):
    model = apps.IntegratedFood.models.collegamento_integredfood_IngredientIF
    fields = ["name", "ingredient",'foodintegratedfoodintegrated']


urlpatterns = FoodIntegratedView.get_urls() + ProfileMediterraneanDietView.get_urls() + IngredientIFView.get_urls() + BromotaologicFactSheetIFView.get_urls() + StepProductionView.get_urls() +collegamento_integredfood_IngredientIFView.get_urls()