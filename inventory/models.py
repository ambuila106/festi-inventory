from django.db import models
from inventory import utils


class Product(models.Model):
    name = models.CharField('Nombre', max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    units_measurement = models.CharField(max_length=10, choices=utils.UNITS_OF_MEASUREMENT)
    amount = models.IntegerField(default=1)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    date = models.DateTimeField()

    def __str__(self):
        return f'Inventory - {self.date.strftime("%Y-%m-%d")}'


class ProductInventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return self.product.name