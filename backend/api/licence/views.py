from django.shortcuts import render
from rest_framework import viewsets

from .models import Licencia
from .serializers import LicenciaSerializer
# Create your views here.

class ViewSetLicencia(viewsets.ModelViewSet):
    """
    ViewSet for Licencia model.
    """
    queryset = Licencia.objects.all()
    serializer_class = LicenciaSerializer
    filterset_fields = ['nombre', 'descripcion', 'fecha_emision']

    my_tags = ['Licencias']