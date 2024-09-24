from django.db import models

# Create your models here.

class Student (models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(default=18)
    email=models.EmailField()
    Address=models.TextField(null=True)
    #Fathername=models.CharField(max_length=50)
    
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField(default=50)
    def __str__(self) -> str:
        return f"{self.name}{self.price}"