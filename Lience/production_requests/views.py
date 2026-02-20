from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import ProductionRequest
from .serializers import ProductionRequestSerializer

class ProductionRequestViewSet(viewsets.ModelViewSet):
    queryset = ProductionRequest.objects.all()
    serializer_class = ProductionRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

# Create your views here.
