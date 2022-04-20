from rest_framework import serializers
from django.db.models import Q
from rest_framework.exceptions import ValidationError
import string

from .models import Country,Sector,FinancedProject

class CountrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Country
        exclude = ['id', 'created_at', 'updated_at']


class SectorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sector
        exclude = ['id', 'created_at', 'updated_at']


class FinancedProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FinancedProject
        exclude = ['id', 'created_at', 'updated_at']

