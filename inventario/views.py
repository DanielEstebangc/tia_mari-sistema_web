from django.shortcuts import render,redirect,get_object_or_404
from .models import Producto
from django.db.models import Sum, Count
from .forms import ProductoForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import EntradaForm, SalidaForm
from .models import Entrada, Salida





def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'inventario/lista_productos.html', {'productos': productos})


def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'inventario/agregar_producto.html', {'form': form})


def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'inventario/editar_producto.html', {'form': form})

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'inventario/eliminar_producto.html', {'producto': producto})


# Vista para registrar una entrada
def registrar_entrada(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            entrada = form.save()
            # Actualizar stock
            producto = entrada.producto
            producto.stock_actual += entrada.cantidad
            producto.save()
            return redirect('lista_productos')  # O donde quieras redirigir
    else:
        form = EntradaForm()
    return render(request, 'inventario/entrada_form.html', {'form': form})

# Vista para registrar una salida
def registrar_salida(request):
    if request.method == 'POST':
        form = SalidaForm(request.POST)
        if form.is_valid():
            salida = form.save()
            producto = salida.producto
            if salida.cantidad <= producto.stock_actual:
                producto.stock_actual -= salida.cantidad
                producto.save()
                return redirect('lista_productos')
            else:
                form.add_error('cantidad', 'Cantidad supera el stock actual.')
    else:
        form = SalidaForm()
    return render(request, 'inventario/salida_form.html', {'form': form})

def ver_movimientos_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    entradas = Entrada.objects.filter(producto=producto).order_by('-fecha')
    salidas = Salida.objects.filter(producto=producto).order_by('-fecha')
    
    return render(request, 'inventario/movimientos_producto.html', {
        'producto': producto,
        'entradas': entradas,
        'salidas': salidas,
    })








def buscar_producto(request):
    query = request.GET.get('q')
    productos = Producto.objects.filter(nombre__icontains=query)
    return render(request, 'inventario/buscar.html', {'productos': productos})

def resumen_inventario(request):
    total_productos = Producto.objects.count()
    total_unidades = Producto.objects.aggregate(Sum('stock'))['stock__sum']
    return render(request, 'inventario/resumen.html', {
        'total_productos': total_productos,
        'total_unidades': total_unidades,
    })

Producto.objects.aaggregate(Sum('stock_actual'), Count('id'))

    
