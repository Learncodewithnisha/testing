from django.db import models

class Recipe(models.Model):
    r_name=models.CharField(max_length=100)
    r_description=models.TextField()
    r_image=models.ImageField(upload_to="recipe")
# Create your models here.
