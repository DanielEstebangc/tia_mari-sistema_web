from django import forms
from .models import Producto
from .models import Entrada, Salida
from .models import Cliente
from .models import Pedido
from .models import ProductoPedido
from django.forms import modelformset_factory



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



class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'observaciones']
        widgets = {
            'observaciones': forms.Textarea(attrs={'rows': 3}),
        }

class ProductoPedidoForm(forms.ModelForm):
    class Meta:
        model = ProductoPedido
        fields = ['producto', 'cantidad']

ProductoPedidoFormSet = modelformset_factory(
    ProductoPedido,
    form=ProductoPedidoForm,
    extra=1,
    can_delete=False
)