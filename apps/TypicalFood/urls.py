from neapolitan.views import CRUDView

import apps.TypicalFood
class GeographicalAreaView(CRUDView):
    model = apps.TypicalFood.models.GeographicalArea
    fields = ["name","climate",'province']

class TypicalityProfileView(CRUDView):
    model = apps.TypicalFood.models.TypicalityProfile
    fields = ["name","geographical_area",'DOP', 'IGP', 'STG']

class BromotaologicFactSheetView(CRUDView):
    model = apps.TypicalFood.models.BromotaologicFactSheet
    fields = ["name", "calories_per_serving","proteins","fats","carbohydrates",'vitamins','minerals','allergens']

class TypicalFoodView(CRUDView):
    model = apps.TypicalFood.models.TypicalFood
    fields = ["name","typicality_profile","bromotaologic_fact_sheet","price","ingredients","serving_size"]


urlpatterns = GeographicalAreaView.get_urls() + TypicalityProfileView.get_urls() + BromotaologicFactSheetView.get_urls() + TypicalFoodView.get_urls()