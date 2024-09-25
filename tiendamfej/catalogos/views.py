from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Producto
from .forms import clienteForm, productoForm

# Create your views here.

#CLIENTES
def homeCliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'homeCliente.html', {'clientes': clientes})

def verCliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'verCliente.html', {'cliente': cliente})

def actualizarCliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        form = clienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('homeCliente')
    else:
        form = clienteForm(instance=cliente)
    return render(request, 'actualizarCliente.html', {'form': form})

def borrarCliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('homeCliente')
    return render(request, 'borrarCliente.html', {'cliente': cliente})

def crearCliente(request):
    if request.method == 'POST':
        form = clienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homeCliente')
    else:
        form = clienteForm()
    return render(request, 'crearCliente.html', {'form': form})


#PRODUCTOS
def homeProducto(request):
    productos = Producto.objects.all()
    return render(request, 'homeProducto.html', {'productos': productos})

# Ver detalles de un producto
def verProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'verProducto.html', {'producto': producto})

# Crear un nuevo producto
def crearProducto(request):
    if request.method == 'POST':
        form = productoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homeProducto')
    else:
        form = productoForm()
    return render(request, 'crearProducto.html', {'form': form})

def actualizarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = productoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('homeProducto')
    else:
        form = productoForm(instance=producto)
    return render(request, 'actualizarProducto.html', {'form': form})

# Borrar un producto
def borrarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('homeProducto')
    return render(request, 'borrarProducto.html', {'producto': producto})