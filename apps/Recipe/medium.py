import uuid
from apps.TypicalFood.models import *
from apps.Recipe.models import *



class MacronutrientsFact:
  def __init__(self, carbs, proteins, fats):
    self.carbs = carbs
    self.proteins = proteins
    self.fats = fats


class MacronutrientsProfile(MacronutrientsFact):
  def __init__(self, carbs: float, proteins: float, fats:float):
    super().__init__(carbs, proteins, fats)



class Ingredient(MacronutrientsProfile):
  # Class variable to store the unique IDs
  _id_counter = 1

  def __init__(self,name: str, carbs: float, proteins: float, fats:float,  calories:float):
    super().__init__(carbs, proteins, fats)
    self.name = name
    self.calories = calories # kcal su 100g
    self.weight = 0 #100gr
    self.id = Ingredient.generate_unique_id()

  @staticmethod
  def generate_unique_id():
    """
    Static method to generate a unique ID for the ingredient.

    :return: A unique ID generated using the `uuid` module.
    """
    unique_id = uuid.uuid4().hex
    return unique_id


def query_nutrienti():
    query = list(TypicalFood.objects.values_list('bromotaologic_fact_sheet_id', flat=True))
    lista = []
    print(query)
    for number in query:
             print(number)
             oggetto = list(BromotaologicFactSheet.objects.filter(id=number).values())
             print(oggetto[0])

             for record in oggetto:
                    name_val = record['name']
                    calories_val = record['calories_per_serving']
                    proteins_val = record['proteins']
                    fats_val = record['fats']
                    carbohydrates_val = record['carbohydrates']

                    Ingredient = (name_val,carbohydrates_val,proteins_val,fats_val,calories_val)

                    lista.append(Ingredient)
                    print(lista)
    return lista


def create_ingredients_list_from_tuples(lista):
    ingredients = []

    for ingredient_tuple in lista:
        name_val, carbohydrates_val, proteins_val, fats_val, calories_val = ingredient_tuple
        ingredient = Ingredient(name_val,carbohydrates_val, proteins_val, fats_val,calories_val)
        ingredients.append(ingredient)

    return ingredients

def check_macronutrient(macro:str,  target, actual,tollerance, kcal_tot):
  target_perc =  getattr(target, macro)
  actual_kcal = getattr(actual, macro)
  actual_perc = actual_kcal / kcal_tot
  tollerance = getattr(tollerance, macro)
  delta_perc = abs(target_perc - actual_perc)
  print(f"{macro} delta %: ", delta_perc)
  if delta_perc <= tollerance:
    return True
  else:
    return False


def get_first_ingredient_sorted_by(ingredients, macronutrient:str):
    ingredients.sort(key=lambda ingredient: (getattr(ingredient, macronutrient)), reverse=True)
    return ingredients[0]


def adjust_macronutrient(main_macronutrient:str, other_macronutrients:list, main_ingredient, actual, target, kcal_tot, remaining_kcal):

    main_macronutrient_value = getattr(main_ingredient, main_macronutrient)
    actual_main_macronutrient = getattr(actual, main_macronutrient)

    target_kcal =  kcal_tot * getattr(target, main_macronutrient)
    print(f"{actual_main_macronutrient} kcal su {target_kcal} necessarie")

    delta_macron_kcal = target_kcal - actual_main_macronutrient
    print("delta_macron_kcal:", delta_macron_kcal)


    print("main_ingredient:", main_ingredient.name)

    delta_weight = delta_macron_kcal/(main_macronutrient_value * main_ingredient.calories)
    main_ingredient.weight += delta_weight
    print(f"{main_ingredient.name}.weight:", main_ingredient.weight)

    actual_main_macronutrient += delta_macron_kcal
    setattr(actual, main_macronutrient, actual_main_macronutrient)
    print(f"actual_{main_macronutrient}:", actual_main_macronutrient)

    for other_macronutrient in other_macronutrients:
      other_macronutrient_value = getattr(main_ingredient, other_macronutrient)
      actual_other_macronutrient = getattr(actual, other_macronutrient)

      actual_other_macronutrient += main_ingredient.weight*other_macronutrient_value * main_ingredient.calories
      setattr(actual, other_macronutrient, actual_other_macronutrient)
      print(f"actual_{other_macronutrient}:", actual_other_macronutrient)

    delta_tot_kcal = delta_weight * main_ingredient.calories
    print(f"ora ci sono {main_ingredient.weight * main_ingredient.calories} kcal di {main_ingredient.name}")


    remaining_kcal -=  delta_tot_kcal
    print("remaining_kcal:", remaining_kcal)

    return(main_ingredient, actual, target, kcal_tot, remaining_kcal,actual_main_macronutrient,actual_other_macronutrient)





def crea_ricetta(ingredients,kcal_tot):

  remaining_kcal = kcal_tot
  target = MacronutrientsProfile(0.5,0.4,0.1)
  actual = MacronutrientsProfile(0,0,0)
  tollerance = MacronutrientsProfile(0.08,0.08,0.08)

  check = MacronutrientsFact(False, False, False)

  total_check = False

  macronutrients = ["carbs","proteins", "fats"]

  recipe = []
  while  total_check == False:

    for macronutrient in macronutrients:
      print("\nmain_macronutrient:", macronutrient)
      other_macronutrients= macronutrients.copy()
      other_macronutrients.remove(macronutrient)
      print("other_macronutrients:", other_macronutrients)

      macronutrient_accepted = check_macronutrient(macronutrient, target, actual,tollerance, kcal_tot)
      print("macronutrient_accepted:", macronutrient_accepted)

      if not macronutrient_accepted:

        main_ingredient =  get_first_ingredient_sorted_by(ingredients, macronutrient)

        main_ingredient, actual, target, kcal_tot, remaining_kcal, actual_main_macronutrient, actual_other_macronutrient = adjust_macronutrient(macronutrient, other_macronutrients, main_ingredient, actual, target, kcal_tot, remaining_kcal)

        print(f"{macronutrient} delta % = 0")
        for other_macronutrient in other_macronutrients:
          check_value = check_macronutrient (other_macronutrient,  target, actual, tollerance, kcal_tot)
          setattr(check, other_macronutrient, check_value)

        #get main ingredient in list and update weight
        main_ingredient_index = [i for i in range(len(ingredients)) if ingredients[i].id == main_ingredient.id]
        main_ingredient_index = main_ingredient_index[0]

        ingredients[main_ingredient_index].weight = main_ingredient.weight


      setattr(check, macronutrient, True)


     # input()

      total_check = all([check.carbs, check.proteins, check.fats])
      print(f"check_carbs:{check.carbs}, check.proteins: {check.proteins}, check.fats: {check.fats}")
      print("total_check:", total_check)

  return ingredients,actual_main_macronutrient,actual_other_macronutrient

def salvo_nel_db_gli_ingredienti(ingredients,actual_main_macronutrient,actual_other_macronutrient,kcal_tot):

    for ingredient in ingredients:
        print("Ingredient:", ingredient)

        print("Name:", ingredient.name)

        print("Unità:", ingredient.weight)

        print("Kcal:", ingredient.calories)

        print("Carboidrati:", ingredient.carbs)

        print("Proteine", ingredient.proteins)

        print("Grassi", ingredient.fats)

        print("Kcal_Totali:", round(ingredient.weight * ingredient.calories))

        print("Peso_in_grammi:", round(ingredient.weight * 100))

        ingrediente_salvato = BromotaologicFactSheetR(
            name=ingredient.name,
            weight=ingredient.weight,
            kcal=ingredient.calories,
            carbs=ingredient.carbs,
            proteins=ingredient.proteins,
            fats=ingredient.fats,
        )
        ingrediente_salvato.save()

    ingrediente_salvato_recipe = RecipeIntegratedMediterraneanFood(
        name="Ricetta generata",
        carbs=(int(kcal_tot)-(int(actual_main_macronutrient)+int(actual_other_macronutrient))),
        proteins=actual_main_macronutrient,
        fats=actual_other_macronutrient
    )
    ingrediente_salvato_recipe.save()



    return ingrediente_salvato.name,ingrediente_salvato_recipe.id

def creazionericettaesalvataggioneldb():
    kcal_tot = 400
    lista = query_nutrienti()
    ingredients = create_ingredients_list_from_tuples(lista)
    ingredients,actual_main_macronutrient,actual_other_macronutrient = crea_ricetta(ingredients,kcal_tot)
    ingrediente_salvato,ingrediente_salvato_recipe_id = salvo_nel_db_gli_ingredienti(ingredients,actual_main_macronutrient,actual_other_macronutrient,kcal_tot)
    return ingrediente_salvato_recipe_id



