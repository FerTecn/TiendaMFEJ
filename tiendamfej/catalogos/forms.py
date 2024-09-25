from django import forms
from .models import Cliente, Producto

class clienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellidos', 'telefono', 'rfc', 'direccion', 'correo_electronico']
        

class productoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['producto', 'categoria', 'precio', 'descripcion']