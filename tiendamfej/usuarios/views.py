from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST['email']  
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)  
        if user is not None:
            login(request, user)
            return redirect('inicio') 
        else:
            return render(request, 'login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'login.html')

def logout(request):
    logout(request)
    return redirect('login')

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Tu cuenta ha sido creada exitosamente.')
            return redirect('usuarios:login.html') 
        else:
            print(form)
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})
