from django.db import models

class Recipe(models.Model):
    name = models.CharField()

class ItemPurchased(models.Model):
    name = models.CharField()
    date_purchased = models.DateField()
    quantity = models.FloatField()
    recipes = models.ManyToManyField(Recipe)



# Create your models here.
