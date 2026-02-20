from django.db import models
from users.models import User
from products.models import Product

class ProductionRequest(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='requests')
    quantity = models.PositiveIntegerField()
    message = models.TextField(blank=True)
    status = models.CharField(max_length=50, default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.buyer.username} requests {self.quantity} of {self.product.name}"

# Create your models here.
