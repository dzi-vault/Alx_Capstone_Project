from django.db import models
from manufacturers.models import ManufacturerProfile

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    manufacturer = models.ForeignKey(ManufacturerProfile, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

# Create your models here.
