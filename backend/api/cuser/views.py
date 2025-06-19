import uuid
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from core.permissions import IsSameOrganizationAndAdmin, IsOwnerOrOrgAdmin

from .serializers import CustomUserSerializer
from .models import CustomUser

class CustomUserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for CustomUser model.
    """
    permission_classes = [IsAuthenticated, IsSameOrganizationAndAdmin]  # Aquí lo agregas
    serializer_class = CustomUserSerializer
    filterset_fields = ['username', 'email', 'first_name', 'last_name', 'organizacion']
    my_tags = ['User Profile']

    def get_queryset(self):
        # Si es staff o admin, puede ver todos los usuarios de la organización
        if self.request.user.is_staff or self.request.user.groups.filter(name='admin').exists():
            return CustomUser.objects.filter(organizacion=self.request.user.organizacion)
        # Si no, solo puede verse a sí mismo
        return CustomUser.objects.filter(id=self.request.user.id)

    def perform_create(self, serializer):
        # Asigna automáticamente la organización del usuario autenticado
        serializer.save(organizacion=self.request.user.organizacion)

    def perform_update(self, serializer):
        # Maneja la actualización de la contraseña
        password = serializer.validated_data.pop('password', None)
        user = serializer.save()
        if password:
            user.set_password(password)
            user.save()


class ProfilePictureView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrOrgAdmin]  # ¡Aquí usas el permiso!
    my_tags = ['User Profile']

    def get(self, request, user_id):
        # Obtiene el usuario (automáticamente 404 si no existe)
        user = get_object_or_404(CustomUser, pk=user_id)
        
        # El permiso IsOwnerOrAdmin ya verificó que request.user == user o es admin
        # Así que no necesitas validar manualmente los permisos aquí.

        if not user.profile_picture:
            raise Http404("El usuario no tiene imagen de perfil")
        
        return FileResponse(user.profile_picture.open('rb'))