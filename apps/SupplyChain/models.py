from django.db import models
from ..TypicalFood.models import TypicalFood
# Create your models here.


class SupplyChain(models.Model):
    """
    Represents a supply chain.

    :param name: The name of the supply chain.
    :type name: str
    :param factors_selection: The factors selection for the supply chain.
    :type factors_selection: FactorsSelectionSupplyChain
    """
    name = models.CharField(max_length=255)
    factors_selection = models.ForeignKey('FactorsSelectionSupplyChain', on_delete=models.CASCADE)
    # Add more fields as per your requirements

    def __str__(self):
        """
        Return a string representation of the supply chain.

        :return: The name of the supply chain.
        :rtype: str
        """
        return self.name


class FactorsSelectionSupplyChain(models.Model):
    """
    Represents the factors selection for a supply chain.

    :param name: The name of the factors selection.
    :type name: str
    """
    name = models.CharField(max_length=255)
    # Add more fields as per your requirements

    def __str__(self):
        """
        Return a string representation of the factors selection.

        :return: The name of the factors selection.
        :rtype: str
        """
        return self.name


class BromotaologicFactSheetSC(models.Model):
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
    # Add more fields as per your requirements
    """
    name = models.CharField(max_length=255)
    calories_per_serving = models.PositiveIntegerField()
    proteins = models.FloatField()
    fats = models.FloatField()
    carbohydrates = models.FloatField()
    vitamins = models.FloatField(default=0)
    minerals = models.FloatField(default=0)
    allergens = models.FloatField(default=0)
    # Add more fields as per your requirements

    def __str__(self):
        """
        Return a string representation of the bromotaologic fact sheet.

        :return: The name of the fact sheet.
        :rtype: str
        """
        return self.name


class SheetNecessityPreprocessing(models.Model):
    """
    Represents a sheet necessity preprocessing.

    :param name: The name of the preprocessing sheet.
    :type name: str
    # Add more fields as per your requirements
    """
    name = models.CharField(max_length=255)
    # Add more fields as per your requirements

    def __str__(self):
        """
        Return a string representation of the sheet necessity preprocessing.

        :return: The name of the preprocessing sheet.
        :rtype: str
        """
        return self.name


class FoodFromTheSupplyChain(models.Model):
    """
    Represents a food item from the supply chain.

    :param name: The name of the food item.
    :type name: str
    :param sheet_necessity_preprocessing: The related sheet necessity preprocessing.
    :type sheet_necessity_preprocessing: SheetNecessityPreprocessing
    :param bromotaologic_fact_sheet: The related bromotaologic fact sheet.
    :type bromotaologic_fact_sheet: BromotaologicFactSheet
    :param supply_chain: The associated supply chain.
    :type supply_chain: SupplyChain
    # Add more fields as per your requirements
    """
    name = models.CharField(max_length=255)
    sheet_necessity_preprocessing = models.ForeignKey('SheetNecessityPreprocessing', on_delete=models.CASCADE)
    bromotaologic_fact_sheet = models.ForeignKey('BromotaologicFactSheetSC', on_delete=models.CASCADE)
    supply_chain = models.ForeignKey('SupplyChain', on_delete=models.CASCADE)
    TypicalFood = models.ForeignKey(TypicalFood, on_delete=models.CASCADE)
    # Add more fields as per your requirements

    def __str__(self):
        """
        Return a string representation of the food item.

        :return: The name of the food item.
        :rtype: str
        """
        return self.name
