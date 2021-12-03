from django.db import models

# Create your models here.


# create a model class for employee table with id name and salary
class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    salary = models.FloatField()

    def __str__(self):
        return self.name
    
# create Student model with id name and score
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    score = models.FloatField()

    def __str__(self):
        return self.name


class Author(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=50)
    ratings = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name='books')
    
    def __str__(self):
        return self.title
    
    