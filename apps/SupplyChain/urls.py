from neapolitan.views import CRUDView

import apps.SupplyChain

class SupplyChainView(CRUDView):
    model = apps.SupplyChain.models.SupplyChain
    fields = ["name", "factors_selection"]

class FactorsSelectionSupplyChainView(CRUDView):
    model = apps.SupplyChain.models.FactorsSelectionSupplyChain
    fields = ["name"]

class BromotaologicFactSheetSCView(CRUDView):
    model = apps.SupplyChain.models.BromotaologicFactSheetSC
    fields = ["name", "calories_per_serving","proteins","fats","carbohydrates",'vitamins','minerals','allergens']

class SheetNecessityPreprocessingView(CRUDView):
    model = apps.SupplyChain.models.SheetNecessityPreprocessing
    fields = ["name"]

class FoodFromTheSupplyChainView(CRUDView):
    model = apps.SupplyChain.models.FoodFromTheSupplyChain
    fields = ["name","sheet_necessity_preprocessing","bromotaologic_fact_sheet","supply_chain","TypicalFood"]



urlpatterns = SupplyChainView.get_urls() + FactorsSelectionSupplyChainView.get_urls() + BromotaologicFactSheetSCView.get_urls() + SheetNecessityPreprocessingView.get_urls() + FoodFromTheSupplyChainView.get_urls()