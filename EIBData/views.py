from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from .serializers import (CountrySerializer, SectorSerializer,FinancedProjectSerializer)


from .models import Country,Sector,FinancedProject

class CountrySerializerViewSet(viewsets.ModelViewSet):
    """Provide CRUD +L functionality for Country."""
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class SectorSerializerViewSet(viewsets.ModelViewSet):
    """Provide CRUD +L functionality for Sector."""
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

class FinancedProjectSerializerViewSet(viewsets.ModelViewSet):
    """Provide CRUD +L functionality for FinancedProject."""
    serializer_class = FinancedProjectSerializer

    def get_queryset(self):
        country_key = self.request.query_params.get('country')
        sector_key = self.request.query_params.get('sector')
        title_key = self.request.query_params.get('project')
        
        filters = Q()
        if(country_key is not None):
            filters &= Q(country=country_key)

        if(sector_key is not None):
            filters &= Q(sector=sector_key)

        if(title_key is not None):
            filters &= Q(title=sectotitle_keyr_key)            

        return FinancedProject.objects.filter(filters)