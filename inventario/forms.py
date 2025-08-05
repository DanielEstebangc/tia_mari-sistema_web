from django import forms
from .models import Producto
from .models import Entrada, Salida
from .models import Cliente


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock_actual']

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['producto', 'cantidad', 'observacion']

class SalidaForm(forms.ModelForm):
    class Meta:
        model = Salida
        fields = ['producto', 'cantidad', 'observacion']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'