from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.homeCliente, name='homeCliente'),
    path('clientes/ver/<int:cliente_id>/', views.verCliente, name='verCliente'),
    path('clientes/actualizar/<int:cliente_id>/', views.actualizarCliente, name='actualizarCliente'),
    path('clientes/borrar/<int:cliente_id>/', views.borrarCliente, name='borrarCliente'),
    path('clientes/crear/', views.crearCliente, name='crearCliente'), 
    
    path('producto', views.homeProducto, name='homeProducto'),
    path('producto/<int:id>/', views.verProducto, name='verProducto'),
    path('producto/nuevo/', views.crearProducto, name='crearProducto'),
    path('producto/actualizar/<int:id>/', views.actualizarProducto, name='actualizarProducto'),
    path('producto/eliminar/<int:id>/', views.borrarProducto, name='borrarProducto'),
]