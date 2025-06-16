from django.db import models

# Create your models here.
class Record(models.Model):
    pedimento = models.ForeignKey('customs.Pedimento', on_delete=models.CASCADE, related_name='records')
    organizacion = models.ForeignKey('organization.Organizacion', on_delete=models.CASCADE, related_name='records')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Record"
        verbose_name_plural = "Records"
        db_table = 'record'
        ordering = ['created_at']

class Document(models.Model):
    organization = models.ForeignKey('organization.Organizacion', on_delete=models.CASCADE, related_name='documents')
    record = models.ForeignKey(Record, on_delete=models.CASCADE, related_name='documents')
    file = models.FileField(upload_to='documents/')
    description = models.CharField(max_length=255, blank=True, null=True)
    size = models.PositiveIntegerField()
    mime_type = models.CharField(max_length=100, blank=True, null=True)

    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.record.name} - {self.file.name}"

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"
        db_table = 'document'
        ordering = ['created_at']

class DocumentByRecord(models.Model):
    organization = models.ForeignKey('organization.Organizacion', on_delete=models.CASCADE, related_name='documents_by_record')
    record = models.ForeignKey(Record, on_delete=models.CASCADE, related_name='document_by_record')
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='document_by_record')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.record.name} - {self.document.file.name}"

    class Meta:
        verbose_name = "Document by Record"
        verbose_name_plural = "Documents by Record"
        db_table = 'document_by_record'
        ordering = ['created_at']