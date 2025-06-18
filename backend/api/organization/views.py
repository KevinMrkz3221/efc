from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.permissions import IsSuperUser
from .serializers import OrganizacionSerializer#, UsuarioOrganizacionSerializer
from .models import Organizacion#, UsuarioOrganizacion

# Create your views here.

class ViewSetOrganizacion(viewsets.ModelViewSet):
    """
    ViewSet for Organizacion model.
    """
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = Organizacion.objects.all()
    serializer_class = OrganizacionSerializer
    filterset_fields = ['nombre', 'descripcion']
    
    my_tags = ['Organizaciones']

