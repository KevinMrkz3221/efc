from django.shortcuts import render
from rest_framework import viewsets

from .serializers import RecordSerializer, DocumentSerializer, DocumentByRecordSerializer
from .models import Record, Document, DocumentByRecord
# Create your views here.

class RecordViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Record model.
    """
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    filterset_fields = ['title', 'description', 'created_at']
    
    my_tags = ['Records']

class DocumentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Document model.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    filterset_fields = ['file', 'description', 'size', 'mime_type']
    
    my_tags = ['Documents']

class ViewSetDocumentByRecord(viewsets.ModelViewSet):
    """
    ViewSet for DocumentByRecord model.
    """
    queryset = DocumentByRecord.objects.all()
    serializer_class = DocumentByRecordSerializer
    filterset_fields = ['record', 'document']
    
    my_tags = ['Documents_By_Record']
    
    def perform_create(self, serializer):
        # Custom logic before saving the instance
        serializer.save()
    
    def perform_update(self, serializer):
        # Custom logic before updating the instance
        serializer.save()