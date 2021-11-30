from django.db import models

# Create your models here.


# create a model class for employee table with id name and salary
class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    salary = models.FloatField()

    def __str__(self):
        return self.name