from django.urls import path
from .views import login, registro, logout

app_name = 'usuarios' 

urlpatterns = [
    path('login/', login, name='login'), 
    path('registro/', registro, name='registro'),
    path('logout/', logout, name='logout'),
]
