from rest_framework import serializers
from .models import ManufacturerProfile

class ManufacturerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManufacturerProfile
        fields = ['id', 'user', 'company_name', 'location', 'contact_email']
