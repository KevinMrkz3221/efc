from django.http import FileResponse, Http404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import CustomUserSerializer
from .models import CustomUser

class CustomUserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for CustomUser model.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer
    filterset_fields = ['username', 'email', 'first_name', 'last_name', 'organizacion']

    my_tags = ['User Profile']

    def get_queryset(self):
        # Devuelve solo el usuario autenticado
        return CustomUser.objects.filter(organizacion=self.request.user.organizacion)
    
    def post(self, request, *args, **kwargs):
        # Permite actualizar el perfil del usuario autenticado
        return self.update(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        # Permite obtener el perfil del usuario autenticado
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        # Permite actualizar el perfil del usuario autenticado
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        # Permite actualizar parcialmente el perfil del usuario autenticado
        return self.partial_update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        # Permite eliminar el perfil del usuario autenticado
        return self.destroy(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        # Permite listar el perfil del usuario autenticado
        if (request.user.is_staff and request.user.is_authenticated and request.user.is_active):
            return super().list(request, *args, **kwargs)
        elif request.user.is_active and request.user.groups.filter(name='admin').exists():
            # Si el usuario no es staff, solo puede ver su propio perfil
            return super().list(request, *args, **kwargs)
        else:
            raise Http404("No autorizado para listar usuarios")
    
    def create(self, request, *args, **kwargs):
        # Permite crear un nuevo perfil de usuario (no recomendado para el usuario autenticado)
        return super().create(request, *args, **kwargs)
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class ProfilePictureView(APIView):
    permission_classes = [IsAuthenticated]

    my_tags = ['User Profile']

    def get_queryset(self):
        # Este método no es necesario aquí, pero se deja por consistencia
        return CustomUser.objects.get(pk=self.request.user.pk)
    def get(self, request, user_id):
        try:
            user = CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            raise Http404("Usuario no encontrado")
        # Opcional: solo el propio usuario o admin puede ver la imagen
        if request.user != user and not request.user.is_staff:
            raise Http404("No autorizado")
        if not user.profile_picture:
            raise Http404("Sin imagen de perfil")
        return FileResponse(user.profile_picture.open('rb'))