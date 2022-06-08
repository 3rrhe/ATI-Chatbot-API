from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    brand = models.CharField(max_length=70,blank=False, default='')
    quantity = models.IntegerField(blank=False, default=0)
    price = models.FloatField(blank=False, default=0)
    iva = models.FloatField(blank=False, default=0)
    priceIva = models.FloatField(blank=False, default=0)