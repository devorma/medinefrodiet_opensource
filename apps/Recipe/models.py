from django.db import models
from ..IntegratedFood.models import FoodIntegrated
from ..Patient.models import MeelRecord
from ..SupplyChain.models import FoodFromTheSupplyChain
# Create your models here.


class BromotaologicFactSheetR(models.Model):
    """
    Represents the bromotaologic fact sheet for an ingredient.

    :param name: The name of the bromatological sheet.
    :type name: str
    :param calories_per_serving: The number of calories per serving.
    :type calories_per_serving: int
    :param proteins: The protein content in grams.
    :type proteins: float
    :param fats: The fat content in grams.
    :type fats: float
    :param carbohydrates: The carbohydrate content in grams.
    :type carbohydrates: float
    :param vitamins: The vitamins present in the food.
    :type vitamins: str
    :param minerals: The minerals present in the food.
    :type minerals: str
    :param allergens: The allergens present in the food.
    :type allergens: str
    """
    name = models.CharField(max_length=255)
    weight = models.FloatField(default=0)
    kcal = models.FloatField(default=0)
    carbs = models.FloatField(default=0)
    proteins = models.FloatField(default=0)
    fats = models.FloatField(default=0)
    kcal_Totali = models.FloatField(default=0)
    peso_in_grammi = models.FloatField(default=0)


    def __str__(self):
        """
        Return a string representation of the bromotaologic fact sheet.

        :return: The name of the fact sheet.
        :rtype: str
        """
        return self.name



    def __str__(self):
        """
        Return a string representation of the ingredient.

        :return: The name of the ingredient.
        :rtype: str
        """
        return self.name

class RecipeIntegratedMediterraneanFood(models.Model):
    """
    Represents an integrated recipe for Mediterranean food.

    :param name: The name of the recipe.
    :type name: str
    :param ingredients: The ingredients used in the recipe.
    :type ingredients: models.ManyToManyField(Ingredient)
    :param food_integrated: The integrated food associated with the recipe.
    :type food_integrated: FoodIntegrated
    :param directions_process_production: The directions for the production process.
    :type directions_process_production: DirectionsProcessProduction
    :param merciological_indications: The merciological indications for the recipe.
    :type merciological_indications: MerciologicalIndications
    :param palatability_sheet: The palatability sheet for the recipe.
    :type palatability_sheet: PalatabilitySheet
    :param meel_record: The meal record associated with the recipe.
    :type meel_record: MeelRecord
    """
    name = models.CharField(max_length=255)
    carbs = models.FloatField(default=0)
    proteins = models.FloatField(default=0)
    fats = models.FloatField(default=0)

    def __str__(self):
        """
        Return a string representation of the integrated Mediterranean food recipe.

        :return: The name of the recipe.
        :rtype: str
        """
        return self.name

class collegamento_recipeintegred_bromotaologicfactsheet(models.Model):
    bromotaologicfactsheet = models.ForeignKey(BromotaologicFactSheetR, on_delete=models.CASCADE)
    recipe = models.ForeignKey(RecipeIntegratedMediterraneanFood, on_delete=models.CASCADE)

    def __str__(self):
        """

        """
        return "collegamento recipeintegred bromotaologicfactsheet"

class DirectionsProcessProduction(models.Model):
    """
    Represents the directions for the production process of an ingredient.

    :param ingredient: The ingredient for which the directions are provided.
    :type ingredient: Ingredient
    :param directions: The directions for the production process.
    :type directions: str
    """
    directions = models.TextField()
    RecipeIntegratedMediterraneanFood = models.ForeignKey(RecipeIntegratedMediterraneanFood, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return a string representation of the directions.

        :return: The name of the ingredient.
        :rtype: str
        """
        return f"Directions for {self.ingredient}"


class MerciologicalIndications(models.Model):
    """
    Represents the merciological indications for the recipe.

    :param indications: The merciological indications.
    :type indications: str
    """
    indications = models.TextField()
    RecipeIntegratedMediterraneanFood = models.ForeignKey(RecipeIntegratedMediterraneanFood, on_delete=models.CASCADE)


    def __str__(self):
        """
        Return a string representation of the merciological indications.

        :return: The merciological indications.
        :rtype: str
        """
        return "Merciological Indications"


class PalatabilitySheet(models.Model):
    """
    Represents the palatability sheet for the recipe.

    :param taste: The taste description.
    :type taste: str
    :param texture: The texture description.
    :type texture: str
    """
    taste = models.TextField()
    texture = models.TextField()
    RecipeIntegratedMediterraneanFood = models.ForeignKey(RecipeIntegratedMediterraneanFood, on_delete=models.CASCADE)


    def __str__(self):
        """
        Return a string representation of the palatability sheet.

        :return: The palatability sheet description.
        :rtype: str
        """
        return "Palatability Sheet"


class collegamento_recipe_integredfood(models.Model):
    food_integrated = models.ForeignKey(FoodIntegrated, on_delete=models.CASCADE)
    recipe = models.ForeignKey(RecipeIntegratedMediterraneanFood, on_delete=models.CASCADE)

    def __str__(self):
        """

        """
        return "Collegamento Recipe Integredfood"
