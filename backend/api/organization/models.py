from django.db import models
from api.licence.models import Licencia


class Organizacion(models.Model):
    id = models.ForeignKey(Licencia, on_delete=models.CASCADE, related_name='organizaciones')
    nombre = models.CharField(max_length=100)
    rfc = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=25)

    calle = models.CharField(max_length=200)
    numero_interior = models.CharField(max_length=100)
    numero_exterior = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    colonia = models.CharField(max_length=50)
    pais = models.CharField(max_length=30)
    estado = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)

    responsable = models.CharField(max_length=400)
    responsable_email = models.EmailField(max_length=100)
    responsable_telefono = models.CharField(max_length=25)
    responsable_puesto = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Organizacion"
        verbose_name_plural = "Organizaciones"
        db_table = 'organizacion'
        ordering = ['nombre']

class UsuarioOrganizacion(models.Model):
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE, related_name='usuarios')
    id_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='usuarios_organizacion')
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=25)
    puesto = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.usuario} - {self.organizacion.nombre}"

    class Meta:
        verbose_name = "Usuario de Organizacion"
        verbose_name_plural = "Usuarios de Organizacion"
        db_table = 'usuario_organizacion'
        ordering = ['usuario']
