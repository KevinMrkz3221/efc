from django.shortcuts import render
from rest_framework import viewsets

from api.customs.models import Pedimento, AgenteAduanal, Aduana, ClavePedimento, TipoOperacion
from api.customs.serializers import PedimentoSerializer, AgenteAduanalSerializer, ClavePedimentoSerializer, AduanaSerializer, TipoOperacionSerializer
# Create your views here.


class ViewSetPedimento(viewsets.ModelViewSet):
    """
    ViewSet for Pedimento model.
    """
    queryset = Pedimento.objects.all()
    serializer_class = PedimentoSerializer
    filterset_fields = ['patente', 'aduana', 'tipo_operacion', 'clave_pedimento']
    search_fields = ['pedimento', 'contribuyente', 'agente_aduanal']
    
    my_tags = ['Pedimentos']

class ViewSetAgenteAduanal(viewsets.ModelViewSet):
    """
    ViewSet for AgenteAduanal model.
    """
    queryset = AgenteAduanal.objects.all()
    serializer_class = AgenteAduanalSerializer
    filterset_fields = ['id_aduana', 'id_patente']

    my_tags = ['Agentes_Aduanales']

class ViewSetAduana(viewsets.ModelViewSet):
    """
    ViewSet for Aduana model.
    """
    queryset = Aduana.objects.all()
    serializer_class = AduanaSerializer
    filterset_fields = ['aduana']
    
    my_tags = ['Aduanas']

class ViewSetClavePedimento(viewsets.ModelViewSet):
    """
    ViewSet for ClavePedimento model.
    """
    queryset = ClavePedimento.objects.all()
    serializer_class = ClavePedimentoSerializer
    filterset_fields = ['clave']
    
    my_tags = ['Claves_Pedimento']

class ViewSetTipoOperacion(viewsets.ModelViewSet):
    """
    ViewSet for TipoOperacion model.
    """
    queryset = TipoOperacion.objects.all()
    serializer_class = TipoOperacionSerializer
    filterset_fields = ['tipo']
    
    my_tags = ['Tipos_Operacion']