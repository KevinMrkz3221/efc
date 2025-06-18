from django.shortcuts import render
from django.http import FileResponse, Http404

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.permissions import IsSameOrganization
from .serializers import DocumentSerializer
from .models import Document
# Create your views here.



class DocumentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Document model.
    """
    permission_classes = [IsAuthenticated, IsSameOrganization]
    
    serializer_class = DocumentSerializer
    filterset_fields = ['archivo', 'descripcion', 'size', 'mime_type']
    
    my_tags = ['Documents']

    def get_queryset(self):
        return Document.objects.filter(organizacion=self.request.user.organizacion)
    
class ProtectedDocumentDownloadView(APIView):
    permission_classes = [IsAuthenticated, IsSameOrganization]
    serializer_class = DocumentSerializer
    my_tags = ['Documents']

    def get_queryset(self):
        return Document.objects.filter(organizacion=self.request.user.organizacion)

    def get(self, request, pk):
        try:
            doc = Document.objects.get(pk=pk)
        except Document.DoesNotExist:
            raise Http404("Documento no encontrado")
        # Verifica que el usuario pertenece a la organización del documento
        if doc.organizacion != request.user.organizacion:
            raise Http404("No autorizado")
        return FileResponse(doc.archivo.open('rb'))
