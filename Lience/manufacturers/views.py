from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import ManufacturerProfile
from .serializers import ManufacturerProfileSerializer

class ManufacturerProfileViewSet(viewsets.ModelViewSet):
    queryset = ManufacturerProfile.objects.all()
    serializer_class = ManufacturerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

# Create your views here.
