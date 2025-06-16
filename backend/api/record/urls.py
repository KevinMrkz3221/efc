# This file defines the URL patterns for the customs app in a Django project.
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# import necessary viewsets
# from .views import YourViewSet  # Import your viewsets here
from .views import RecordViewSet, DocumentViewSet, ViewSetDocumentByRecord
# Create a router and register your viewsets with it

router = DefaultRouter()

# Register your viewsets with the router here
# Example:
# from .views import MyViewSet
# router.register(r'myviewset', MyViewSet, basename='myviewset')
router.register(r'records', RecordViewSet, basename='Record')
router.register(r'documents', DocumentViewSet, basename='Document')
router.register(r'documents_by_record', ViewSetDocumentByRecord, basename='DocumentByRecord')
# Import your viewsets here

urlpatterns = [
    path('', include(router.urls)),
]