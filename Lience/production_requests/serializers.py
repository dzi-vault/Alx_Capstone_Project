from rest_framework import serializers
from .models import ProductionRequest

class ProductionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionRequest
        fields = ['id', 'buyer', 'product', 'quantity', 'message', 'status', 'timestamp']
