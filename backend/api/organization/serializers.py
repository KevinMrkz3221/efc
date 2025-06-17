from rest_framework import serializers

from .models import Organizacion#, UsuarioOrganizacion

class OrganizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizacion
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

# class UsuarioOrganizacionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UsuarioOrganizacion
#         fields = '__all__'
#         read_only_fields = ('created_at', 'updated_at')

#     def validate(self, attrs):
#         if not attrs.get('usuario'):
#             raise serializers.ValidationError("El campo 'usuario' es obligatorio.")
#         if not attrs.get('organizacion'):
#             raise serializers.ValidationError("El campo 'organizacion' es obligatorio.")
#         return attrs