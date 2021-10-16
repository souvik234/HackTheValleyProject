import datetime

from django.db import models

expiryDict={
    'Apples': 7,
    'Milk': 30,
    'Bananas': 7,
    'Eggs': 14,
    'lettuce': 12


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
