from django.urls import path
from . import views

urlpatterns = [
    # Rutas para productos
    path('', views.lista_productos, name='lista_productos'),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),    
    path('editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('entrada/', views.registrar_entrada, name='registrar_entrada'),
    path('salida/', views.registrar_salida, name='registrar_salida'),
    path('producto/<int:producto_id>/movimientos/', views.ver_movimientos_producto, name='ver_movimientos_producto'),
    path('buscar/', views.buscar_producto, name='buscar_producto'),
    path('resumen/', views.resumen_inventario, name='resumen_inventario'),
    # Rutas para clientes
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),

]