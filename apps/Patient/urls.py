from neapolitan.views import CRUDView
import apps.Patient

class PatientView(CRUDView):
    model = apps.Patient.models.Patient
    fields = ["name", "age", "gender","meel_record","medical_history"]



class MeelRecordView(CRUDView):
    model = apps.Patient.models.MeelRecord
    fields = ["name", "description","meal_date","calories","proteins","fats","carbohydrates"]




urlpatterns = PatientView.get_urls() + MeelRecordView.get_urls()