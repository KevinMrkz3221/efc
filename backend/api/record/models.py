from django.db import models
import uuid
# Create your models here.

class Document(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    organizacion = models.ForeignKey('organization.Organizacion', on_delete=models.CASCADE, related_name='documents')
    pedimento = models.ForeignKey('customs.Pedimento', on_delete=models.CASCADE, related_name='documents')
    archivo = models.FileField(upload_to='documents/', max_length=400)
    document_type = models.ForeignKey('DocumentType', on_delete=models.CASCADE, related_name='documents', blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    extension = models.CharField(max_length=10, blank=True, null=True)
    size = models.PositiveIntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.archivo.name}"

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"
        db_table = 'document'
        ordering = ['created_at']

class DocumentType(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Tipo de Documento"
        verbose_name_plural = "Tipos de Documento"
        db_table = 'document_type'
        ordering = ['nombre']