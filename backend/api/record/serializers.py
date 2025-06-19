from rest_framework import serializers

from .models import Document



class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def validate(self, attrs):
        print(attrs)
        if not attrs.get('archivo'):
            raise serializers.ValidationError("El campo 'file' es obligatorio.")
        if not attrs.get('organizacion'):
            raise serializers.ValidationError("El campo 'organizacion' es obligatorio.")
        return attrs

