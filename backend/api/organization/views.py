from django.shortcuts import render
from rest_framework import viewsets

from .serializers import OrganizacionSerializer#, UsuarioOrganizacionSerializer
from .models import Organizacion#, UsuarioOrganizacion

# Create your views here.

class ViewSetOrganizacion(viewsets.ModelViewSet):
    """
    ViewSet for Organizacion model.
    """
    queryset = Organizacion.objects.all()
    serializer_class = OrganizacionSerializer
    filterset_fields = ['nombre', 'descripcion']
    
    my_tags = ['Organizaciones']

# class ViewSetUsuarioOrganizacion(viewsets.ModelViewSet):
#     """
#     ViewSet for UsuarioOrganizacion model.
#     """
#     queryset = UsuarioOrganizacion.objects.all()
#     serializer_class = UsuarioOrganizacionSerializer
#     filterset_fields = ['usuario', 'organizacion']
    
#     my_tags = ['Usuarios_Organizaciones']
    
#     def perform_create(self, serializer):
#         # Custom logic before saving the instance
#         serializer.save()
    
#     def perform_update(self, serializer):
#         # Custom logic before updating the instance
#         serializer.save()