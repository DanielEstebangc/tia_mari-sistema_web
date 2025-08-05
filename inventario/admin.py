from django.contrib import admin
from .models import Producto, Entrada, Salida,Cliente


# Opcional: mostrar campos específicos en la lista del admin
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock_actual', 'fecha_creacion')
    search_fields = ('nombre',)

class EntradaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad', 'fecha', 'observacion')
    search_fields = ('producto__nombre',)

class SalidaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad', 'fecha', 'observacion')
    search_fields = ('producto__nombre',)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'telefono', 'direccion', 'fecha_registro')
    search_fields = ('nombre',)

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Salida, SalidaAdmin)
admin.site.register(Cliente, ClienteAdmin)
