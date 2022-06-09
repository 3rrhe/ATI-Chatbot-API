from django.db import models


# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=70, blank=False, default='')
    last_name = models.CharField(max_length=70, blank=False, default='')
    address = models.CharField(max_length=70, blank=False, default=0)
    phone = models.CharField(max_length=70, blank=False, default=0)

class Brand(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=70, blank=False, default='')

class Product(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    brand = models.CharField(max_length=70, blank=False, default='')
    quantity = models.IntegerField(blank=False, default=0)
    price = models.FloatField(blank=False, default=0)
    iva = models.FloatField(blank=False, default=0)
    priceIva = models.FloatField(blank=False, default=0)
    image = models.TextField(blank=False, default="")