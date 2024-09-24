from django.urls import path
from . import views

urlpatterns = [
    path('cliente/', views.homeCliente, name='homeCliente'),
    path('clientes/ver/<int:cliente_id>/', views.verCliente, name='verCliente'),
    path('clientes/actualizar/<int:cliente_id>/', views.actualizarCliente, name='actualizarCliente'),
    path('clientes/borrar/<int:cliente_id>/', views.borrarCliente, name='borrarCliente'),
    path('clientes/crear/', views.crearCliente, name='crearCliente'), 
    
    
]