from rest_framework import serializers
from api.customs.models import Pedimento, Aduana, AgenteAduanal, ClavePedimento, TipoOperacion
from api.record.models import Document  # Asegúrate de importar el modelo Documento
from api.record.serializers import DocumentoSerializer  

class PedimentoSerializer(serializers.ModelSerializer):
    documentos = DocumentoSerializer(many=True, read_only=True, source='documents')

    class Meta:
        model = Pedimento
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class AgenteAduanalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgenteAduanal
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class AduanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aduana
        fields = '__all__'

class ClavePedimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClavePedimento
        fields = '__all__'

class TipoOperacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoOperacion
        fields = '__all__'