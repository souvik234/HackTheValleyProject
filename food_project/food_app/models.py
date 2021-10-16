from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)

class ItemPurchased(models.Model):
    name = models.CharField(max_length=100)
    date_purchased = models.DateField()
    quantity = models.FloatField()
    photo = models.ImageField(upload_to='items')

    expiry_date = date_purchased.date()
    def __str__(self):
        return self.name



# Create your models here.
