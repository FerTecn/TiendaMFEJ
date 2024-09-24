from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import clienteForm

# Create your views here.
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


