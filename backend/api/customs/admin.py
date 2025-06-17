from django.contrib import admin
from .models import Aduana, ClavePedimento, TipoOperacion, Pedimento, AgenteAduanal, Patente
# Register your models here.

class PatenteAdmin(admin.ModelAdmin):
    model = Patente
    list_display = ('id', 'numero', 'descripcion')
    search_fields = ('numero', 'descripcion')

class AduanaAdmin(admin.ModelAdmin):
    model = Aduana
    list_display = ('id', 'seccion',)
    search_fields = ('nombre', 'codigo')

class ClavePedimentoAdmin(admin.ModelAdmin):
    model = ClavePedimento
    list_display = ('id', 'clave')
    search_fields = ('clave', 'descripcion')


class TipoOperacionAdmin(admin.ModelAdmin):
    model = TipoOperacion
    list_display = ('id', 'tipo')
    search_fields = ('nombre',)

class PedimentoAdmin(admin.ModelAdmin):
    model = Pedimento
    list_display = ('id', 'pedimento', 'aduana', 'patente')
    search_fields = ('numero',)
    list_filter = ('aduana', 'agente_aduanal')

class AgenteAduanalAdmin(admin.ModelAdmin):
    model = AgenteAduanal
    list_display = ('id', 'id_aduana', 'id_patente', 'nombre', 'rfc')
    search_fields = ('nombre', 'rfc')

admin.site.register(Aduana, AduanaAdmin)
admin.site.register(ClavePedimento, ClavePedimentoAdmin)
admin.site.register(TipoOperacion, TipoOperacionAdmin)
admin.site.register(Pedimento, PedimentoAdmin)
admin.site.register(AgenteAduanal, AgenteAduanalAdmin)
admin.site.register(Patente, PatenteAdmin)