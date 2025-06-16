from django.db import models

# Create your models here.
class Aduana(models.Model):
    seccion = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Aduana"
        verbose_name_plural = "Aduanas"
        db_table = 'aduana'
        ordering = ['seccion']

class ClavePedimento(models.Model):
    clave = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Clave de Pedimento"
        verbose_name_plural = "Claves de Pedimento"
        db_table = 'clave_pedimento'
        ordering = ['clave']

class TipoOperacion(models.Model):
    tipo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Tipo de Operacion"
        verbose_name_plural = "Tipos de Operacion"
        db_table = 'tipo_operacion'
        ordering = ['tipo']

class Pedimento(models.Model):
    organizacion = models.ForeignKey('organization.Organizacion', on_delete=models.CASCADE, related_name='pedimentos')
    pedimento = models.CharField(max_length=20)
    patente = models.CharField(max_length=10)
    aduana = models.ForeignKey(Aduana, on_delete=models.CASCADE, related_name='pedimentos')
    tipo_operacion = models.ForeignKey(TipoOperacion, on_delete=models.CASCADE, related_name='pedimentos')
    clave_pedimento = models.ForeignKey(ClavePedimento, on_delete=models.CASCADE, related_name='pedimentos')

    fechapago = models.DateField()
    contribuyente = models.CharField(max_length=100)
    agente_aduanal = models.CharField(max_length=100)
    alerta = models.BooleanField(default=False)
    curp_apoderado = models.CharField(max_length=18, blank=True, null=True)

    importe_total = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_disponible = models.DecimalField(max_digits=10, decimal_places=2)
    importe_pedimento = models.DecimalField(max_digits=10, decimal_places=2)
    existe_expediente = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = "Pedimento"
        verbose_name_plural = "Pedimentos"
        db_table = 'pedimento'
        ordering = ['pedimento']

class AgenteAduanal(models.Model):
    id_aduana = models.ForeignKey(Aduana, on_delete=models.CASCADE, related_name='agentes_aduanales')
    id_patente = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    rfc = models.CharField(max_length=13, blank=True, null=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Agente Aduanal"
        verbose_name_plural = "Agentes Aduanales"
        db_table = 'agente_aduanal'
        ordering = ['nombre']