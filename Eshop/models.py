from django.db import models

class E_Shop(models.Model):
    Productname = models.CharField(max_length = 250)
    price = models.DecimalField( max_digits=5, decimal_places=2)
    Quantity = models.CharField(max_length = 1000)
    image = models.CharField(max_length =2500)

