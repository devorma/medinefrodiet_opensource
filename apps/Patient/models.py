from django.db import models

# Create your models here.

class Patient(models.Model):
    """
    Represents a patient.

    :param name: The name of the patient.
    :type name: str
    :param age: The age of the patient.
    :type age: int
    :param gender: The gender of the patient.
    :type gender: str
    :param meel_record: The meal record associated with the patient.
    :type meel_record: MeelRecord
    :param medical_history: The medical history of the patient.
    :type medical_history: str
    """
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    meel_record = models.ForeignKey('MeelRecord', on_delete=models.CASCADE)
    medical_history = models.TextField()

    def __str__(self):
        """
        Return a string representation of the patient.

        :return: The name of the patient.
        :rtype: str
        """
        return self.name


class MeelRecord(models.Model):
    """
    Represents a record of the meal.

    :param name: The name of the meal.
    :type name: str
    :param description: The description of the meal.
    :type description: str
    :param meal_date: The date of the meal.
    :type meal_date: datetime.date
    :param calories: The total calories of the meal.
    :type calories: int
    :param proteins: The total proteins of the meal.
    :type proteins: float
    :param fats: The total fats of the meal.
    :type fats: float
    :param carbohydrates: The total carbohydrates of the meal.
    :type carbohydrates: float
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    meal_date = models.DateField()
    calories = models.PositiveIntegerField()
    proteins = models.FloatField()
    fats = models.FloatField()
    carbohydrates = models.FloatField()

    def __str__(self):
        """
        Return a string representation of the meal record.

        :return: The name of the meal.
        :rtype: str
        """
        return self.name
