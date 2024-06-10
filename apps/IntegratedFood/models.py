from django.db import models

# Create your models here.

class StepProduction(models.Model):
    """
    Represents a step in the production process of an ingredient.

    :param name: The name of the production step.
    :type name: str
    :param description: The description of the production step.
    :type description: str
    """
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        """
        Return a string representation of the step in production.

        :return: The name of the production step.
        :rtype: str
        """
        return self.name


class BromotaologicFactSheetIF(models.Model):
    """
    Represents a bromotaologic fact sheet for an ingredient.

    :param name: The name of the fact sheet.
    :type name: str
    :param calories_per_serving: The number of calories per serving.
    :type calories_per_serving: int
    :param proteins: The protein content in grams.
    :type proteins: decimal.Decimal
    :param fats: The fat content in grams.
    :type fats: decimal.Decimal
    :param carbohydrates: The carbohydrate content in grams.
    :type carbohydrates: decimal.Decimal
    :param vitamins: The vitamins present in the ingredient.
    :type vitamins: str
    :param minerals: The minerals present in the ingredient.
    :type minerals: str
    :param allergens: The allergens present in the ingredient.
    :type allergens: str
    """
    name = models.CharField(max_length=255)
    calories_per_serving = models.PositiveIntegerField()
    proteins = models.FloatField()
    fats = models.FloatField()
    carbohydrates = models.FloatField()
    vitamins = models.FloatField(default=0)
    minerals = models.FloatField(default=0)
    allergens = models.FloatField(default=0)

    def __str__(self):
        """
        Return a string representation of the bromotaologic fact sheet.

        :return: The name of the fact sheet.
        :rtype: str
        """
        return self.name


class IngredientIF(models.Model):
    """
    Represents an ingredient used in food preparation.

    :param name: The name of the ingredient.
    :type name: str
    :param step_production: The production step for the ingredient.
    :type step_production: StepProduction
    :param bromotaologic_fact_sheet: The bromotaologic fact sheet for the ingredient.
    :type bromotaologic_fact_sheet: BromotaologicFactSheet
    """
    name = models.CharField(max_length=255)
    step_production = models.ForeignKey(StepProduction, on_delete=models.CASCADE, default=0)
    bromotaologic_fact_sheet = models.ForeignKey('BromotaologicFactSheetIF', on_delete=models.CASCADE)

    def __str__(self):
        """
        Return a string representation of the ingredient.

        :return: The name of the ingredient.
        :rtype: str
        """
        return self.name


class ProfileMediterraneanDiet(models.Model):
    """
    Represents a profile for the Mediterranean diet.

    :param name: The name of the profile.
    :type name: str
    :param description: The description of the profile.
    :type description: str
    """
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        """
        Return a string representation of the Mediterranean diet profile.

        :return: The name of the profile.
        :rtype: str
        """
        return self.name



class FoodIntegrated(models.Model):
    """
    Represents an integrated food item.

    :param name: The name of the food item.
    :type name: str
    :param ingredient: The ingredient used in the food item.
    :type ingredient: Ingredient
    :param profile_mediterranean_diet: The Mediterranean diet profile associated with the food item.
    :type profile_mediterranean_diet: ProfileMediterraneanDiet
    :param recipe_integrated_mediterranean_food: The integrated Mediterranean food recipe associated with the food item.
    :type recipe_integrated_mediterranean_food: RecipeIntegratedMediterraneanFood
    :param price: The price of the food item.
    :type price: decimal.Decimal
    :param expiry_date: The expiry date of the food item.
    :type expiry_date: datetime.date
    """
    name = models.CharField(max_length=255)
    profile_mediterranean_diet = models.ForeignKey(ProfileMediterraneanDiet, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    expiry_date = models.DateField()

    def __str__(self):
        """
        Return a string representation of the integrated food item.

        :return: The name of the food item.
        :rtype: str
        """
        return self.name


class collegamento_integredfood_IngredientIF(models.Model):
    name = models.CharField(max_length=255)
    ingredient = models.ForeignKey(IngredientIF, on_delete=models.CASCADE)
    foodintegrated = models.ForeignKey(FoodIntegrated, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return a string representation of the integrated food item.

        :return: The name of the food item.
        :rtype: str
        """
        return self.name
