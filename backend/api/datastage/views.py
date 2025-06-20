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
        Returns DataStages only for the requesting user's organization.
        """
        return DataStage.objects.filter(organizacion=self.request.user.organizacion)
    
    