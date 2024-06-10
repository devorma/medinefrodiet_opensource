from django.db import models

# Create your models here.

class GeographicalArea(models.Model):
    """
    Represents a geographical area.

    :param name: The name of the geographical area.
    :type name: str
    :param climate: The climate of the geographical area.
    :type climate: str
    :param population: The population count of the geographical area.
    :type population: int
    :param language: The primary language spoken in the geographical area.
    :type language: str
    """

    name = models.CharField(max_length=255)
    climate = models.CharField(max_length=100)
    province = models.CharField(max_length=2)



    def __str__(self):
        """
        Return a string representation of the geographical area.

        :return: The name of the geographical area.
        :rtype: str
        """
        return self.name


class BromotaologicFactSheet(models.Model):
    """
    Represents a bromotaologic fact sheet.

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


class TypicalityProfile(models.Model):
    """
    Represents a typicality profile.

    :param name: The name of the typicality profile.
    :type name: str
    :param geographical_area: The associated geographical area.
    :type geographical_area: GeographicalArea
    :param typicality_score: The typicality score.
    :type typicality_score: decimal.Decimal
    """

    name = models.CharField(max_length=255)
    geographical_area = models.ForeignKey(GeographicalArea, on_delete=models.CASCADE)
    DOP = models.BooleanField(default=False)
    IGP = models.BooleanField(default=False)
    STG = models.BooleanField(default=False)

    def __str__(self):
        """
        Return a string representation of the typicality profile.

        :return: The name of the typicality profile.
        :rtype: str
        """
        return self.name


class TypicalFood(models.Model):
    """
    Represents a typical food item.

    :param name: The name of the food item.
    :type name: str
    :param typicality_profile: The associated typicality profile.
    :type typicality_profile: TypicalityProfile
    :param bromotaologic_fact_sheet: The associated bromotaologic fact sheet.
    :type bromotaologic_fact_sheet: BromotaologicFactSheet
    :param price: The price of the food item.
    :type price: decimal.Decimal
    :param ingredients: The list of ingredients.
    :type ingredients: str
    :param serving_size: The serving size description.
    :type serving_size: str
    """

    name = models.CharField(max_length=255)
    typicality_profile = models.ForeignKey(TypicalityProfile, on_delete=models.CASCADE)
    bromotaologic_fact_sheet = models.ForeignKey(BromotaologicFactSheet, on_delete=models.CASCADE, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    ingredients = models.TextField()
    serving_size = models.CharField(max_length=50)


    def __str__(self):
        """
        Return a string representation of the typical food item.

        :return: The name of the food item.
        :rtype: str
        """
        return self.name
