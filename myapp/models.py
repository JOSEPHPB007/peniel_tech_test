from django.db import models


class Members(models.Model):
    name=models.CharField(max_length=100)
    discount=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name

class Product(models.Model):
    productname=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.productname