from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.permissions import IsSameOrganizationAndAdmin
from .models import DataStage
from .serializer import DataStageSerializer
# Create your views here.

class DataStageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing DataStage instances.
    Provides CRUD operations for DataStage.
    """
    
    serializer_class = DataStageSerializer
    permission_classes = [IsAuthenticated, IsSameOrganizationAndAdmin]

    my_tags = ['DataStage']

    def get_queryset(self):
        """
        Optionally restricts the returned DataStages to a given organization,
        by filtering against a 'organizacion' query parameter in the URL.
        """
        queryset = DataStage.objects.filter(organizacion = self.request.user.organizacion)
        organizacion_id = self.request.query_params.get('organizacion', None)
        if organizacion_id is not None:
            queryset = queryset.filter(organizacion_id=organizacion_id)
        return queryset
    
    