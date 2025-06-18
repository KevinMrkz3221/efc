# permissions.py
from rest_framework import permissions


class IsSameOrganization(permissions.BasePermission):
    """
    Permiso personalizado que solo permite acceder a usuarios de la misma organización
    o a administradores/staff.
    """
    def has_permission(self, request, view):
        # Permite listar/crear solo si el usuario está autenticado
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Permite operaciones sobre un objeto específico solo si:
        # - El objeto pertenece a la misma organización
        return (obj.organizacion == request.user.organizacion) 
    
class IsSameOrganizationAndAdmin(permissions.BasePermission):
    """
    Permiso personalizado que solo permite acceder a usuarios de la misma organización
    o a administradores/staff.
    """
    def has_permission(self, request, view):
        # Permite listar/crear solo si el usuario está autenticado
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Permite operaciones sobre un objeto específico solo si:
        # - El objeto pertenece a la misma organización
        return (obj.organizacion == request.user.organizacion) and \
               request.user.groups.filter(name='admin').exists()

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff
    
class IsSuperUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser