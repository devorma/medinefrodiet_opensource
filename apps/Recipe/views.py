from django.shortcuts import render
from apps.Recipe.models import *
from apps.IntegratedFood.models import *
# Create your views here .
from apps.Recipe.medium import creazionericettaesalvataggioneldb

def crearicetta(request):
    ricetta=creazionericettaesalvataggioneldb()
    inforicetta = list(RecipeIntegratedMediterraneanFood.objects.filter(id=ricetta).values())
    context = {
        'ricetta': inforicetta,
    }

    return render(request, 'Recipe/Recipe_detail.html', context)


def consultaricetta(request):

    inforicetta = list(RecipeIntegratedMediterraneanFood.objects.values())
    context = {
        'ricetta': inforicetta,
    }

    return render(request, 'Recipe/Recipe.html', context)


id_ricetta = 10
def dettaglio_ricetta(request):

    food_integrated = list(collegamento_recipeintegred_bromotaologicfactsheet.objects.filter(recipe_id=10).values())
    lista_brom=[]
    for item in food_integrated:
        print(item)

        sched_bromat = list(BromotaologicFactSheetR.objects.filter(id=item['bromotaologicfactsheet_id']).values())

        lista_brom.append(sched_bromat[0])

    context = {
        'lista_brom': lista_brom,
    }

    return render(request, 'Recipe/Recipe_info.html', context)




