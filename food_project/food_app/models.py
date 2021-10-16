import datetime

from django.db import models

expiryDict={
    'Apples': 7,
    'Milk': 30,
    'Bananas': 7,
    'Eggs': 14,
    'Lettuce': 12,
    'Flour': 180,
    'Onions': 7,
    'Potatoes': 90,
    'Cheese': 10,
    'Nutmeg': 365,
    'Carrots': 31,
    'Lentils': 365,
    'Spinach': 14,
    'Walnuts': 365,
    'Turkey': 3,
    'Butter': 14,
    'Chicken': 3,
}

class Recipe(models.Model):
    name = models.CharField(max_length=100)

class ItemPurchased(models.Model):
    name = models.CharField(max_length=100)
    date_purchased = models.DateField()
    quantity = models.FloatField()
    photo = models.ImageField(upload_to='items')

    expiry_date = models.DateField(blank=True, null=True)


    def clean(self):
        if not self.expiry_date:
            self.expiry_date = self.date_purchased + datetime.timedelta(days=expiryDict['Apples'])

    def save(self, **kwargs):
        self.clean()
        return super().save(**kwargs)


    def __str__(self):
        return self.name



# Create your models here.
