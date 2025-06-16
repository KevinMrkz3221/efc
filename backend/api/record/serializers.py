from rest_framework import serializers

from .models import Record, Document, DocumentByRecord

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def validate(self, attrs):
        if not attrs.get('file'):
            raise serializers.ValidationError("El campo 'file' es obligatorio.")
        if not attrs.get('organization'):
            raise serializers.ValidationError("El campo 'organization' es obligatorio.")
        return attrs

class DocumentByRecordSerializer(serializers.ModelSerializer): 
    class Meta:
        model = DocumentByRecord
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def validate(self, attrs):
        if not attrs.get('record'):
            raise serializers.ValidationError("El campo 'record' es obligatorio.")
        if not attrs.get('document'):
            raise serializers.ValidationError("El campo 'document' es obligatorio.")
        return attrs