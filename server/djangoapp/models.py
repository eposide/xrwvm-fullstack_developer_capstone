# Uncomment the following imports before adding the Model code
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):

    name = models.CharField(null=False, max_length=30)
    description = models.CharField(null=False, max_length=100)

    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.description


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    CAR_TYPE_CHOICES = {
        "SEDAN": "Sedan",
        "SUV": "SUV",
        "WAGON": "Wagon",
        "TRUCK": "Truck",
    }

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=30)
    type = models.CharField(null=False, max_length=30,
                            choices=CAR_TYPE_CHOICES, default="Sedan")
    year = models.IntegerField(null=False,
                               validators=[MinValueValidator(2015),
                                           MaxValueValidator(2023)])


def __str__(self):
    return "Name: " + self.name + "," + \
            "Type: " + self.type + "," + \
            "Year: " + str(self.year) + "," + \
            "Car Make: " + str(self.car_make.name)
