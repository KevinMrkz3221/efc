import uuid
from django.db import models

# Create your models here.
class Aduana(models.Model):
    seccion = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.seccion}"
    
    class Meta:
        verbose_name = "Aduana"
        verbose_name_plural = "Aduanas"
        db_table = 'aduana'
        ordering = ['seccion']

class Patente(models.Model):
    numero = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.numero}"

    class Meta:
        verbose_name = "Patente"
        verbose_name_plural = "Patentes"
        db_table = 'patente'
        ordering = ['numero']
    
    
class ClavePedimento(models.Model):
    clave = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.clave}"

    class Meta:
        verbose_name = "Clave de Pedimento"
        verbose_name_plural = "Claves de Pedimento"
        db_table = 'clave_pedimento'
        ordering = ['clave']

class TipoOperacion(models.Model):
    tipo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.tipo}"

    class Meta:
        verbose_name = "Tipo de Operacion"
        verbose_name_plural = "Tipos de Operacion"
        db_table = 'tipo_operacion'
        ordering = ['tipo']

class Pedimento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organizacion = models.ForeignKey('organization.Organizacion', on_delete=models.CASCADE, related_name='pedimentos')
    pedimento = models.CharField(max_length=20)
    patente = models.ForeignKey('Patente', on_delete=models.CASCADE, related_name='pedimentos')
    aduana = models.ForeignKey(Aduana, on_delete=models.CASCADE, related_name='pedimentos')
    tipo_operacion = models.ForeignKey(TipoOperacion, on_delete=models.CASCADE, related_name='pedimentos')
    clave_pedimento = models.ForeignKey(ClavePedimento, on_delete=models.CASCADE, related_name='pedimentos')

    fechapago = models.DateField()
    contribuyente = models.CharField(max_length=100)
    agente_aduanal = models.ForeignKey('AgenteAduanal', on_delete=models.CASCADE, related_name='pedimentos', blank=True, null=True)
    alerta = models.BooleanField(default=False)
    curp_apoderado = models.CharField(max_length=18, blank=True, null=True)

    importe_total = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_disponible = models.DecimalField(max_digits=10, decimal_places=2)
    importe_pedimento = models.DecimalField(max_digits=10, decimal_places=2)
    existe_expediente = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.aduana.seccion} - {self.patente}-{self.pedimento} "

    class Meta:
        verbose_name = "Pedimento"
        verbose_name_plural = "Pedimentos"
        db_table = 'pedimento'
        ordering = ['pedimento']

class AgenteAduanal(models.Model):
    id_aduana = models.ForeignKey(Aduana, on_delete=models.CASCADE, related_name='agentes_aduanales')
    id_patente = models.ForeignKey('Patente', on_delete=models.CASCADE, related_name='agentes_aduanales')
    nombre = models.CharField(max_length=100)
    rfc = models.CharField(max_length=13, blank=True, null=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} - ({self.id_patente})"

    class Meta:
        verbose_name = "Agente Aduanal"
        verbose_name_plural = "Agentes Aduanales"
        db_table = 'agente_aduanal'
        ordering = ['nombre']