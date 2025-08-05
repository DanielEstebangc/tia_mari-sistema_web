from django.shortcuts import render,redirect,get_object_or_404
from .models import Producto, Entrada, Salida, Cliente,  Pedido
from django.db.models import Sum, Count
from .forms import ProductoForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import EntradaForm, SalidaForm, ClienteForm, PedidoForm
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .models import Pedido, ProductoPedido, Producto
from .forms import PedidoForm, ProductoPedidoFormSet
from django.db import transaction






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

Producto.objects.aggregate(Sum('stock_actual'), Count('id'))


# Vistas para registrar un cliente
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('lista_clientes')
            except IntegrityError:
                form.add_error('correo', 'Este correo ya está registrado.')
        # Si no es válido, se vuelve a mostrar el formulario con errores
    else:
        form = ClienteForm()
    
    return render(request, 'clientes/agregar_cliente.html', {'form': form})

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/editar_cliente.html', {'form': form})

def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'clientes/eliminar_cliente.html', {'cliente': cliente})
    

def lista_pedidos(request):
    pedidos = Pedido.objects.select_related('cliente').order_by('-fecha')
    return render(request, 'pedidos/lista_pedidos.html', {'pedidos': pedidos})

@transaction.atomic
def crear_pedido(request):
    if request.method == 'POST':
        pedido_form = PedidoForm(request.POST)
        formset = ProductoPedidoFormSet(request.POST, queryset=ProductoPedido.objects.none())

        if pedido_form.is_valid() and formset.is_valid():
            pedido = pedido_form.save()

            for form in formset:
                producto = form.cleaned_data.get('producto')
                cantidad = form.cleaned_data.get('cantidad')

                if producto and cantidad:
                    # Crear relación producto-pedido
                    ProductoPedido.objects.create(
                        pedido=pedido,
                        producto=producto,
                        cantidad=cantidad
                    )

                    # Actualizar stock
                    producto.stock_actual -= cantidad
                    producto.save()

            return redirect('lista_pedidos')  # Cambia según tu nombre de URL

    else:
        pedido_form = PedidoForm()
        formset = ProductoPedidoFormSet(queryset=ProductoPedido.objects.none())

    return render(request, 'pedidos/crear_pedido.html', {
        'pedido_form': pedido_form,
        'formset': formset
    })

def inicio(request):
    return render(request, 'inicio.html')