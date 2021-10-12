from django.db import models

class Item(models.Model):
  name = models.CharField(max_length=30)
  manufacturer = models.CharField(max_length=50)
  cost = models.DecimalField(max_digits=10, decimal_places=2)
  weight = models.FloatField()
  image = models.CharField(max_length=100)
  