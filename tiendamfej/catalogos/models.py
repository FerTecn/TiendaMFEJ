from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    telefono = models.CharField(max_length=15)
    rfc = models.CharField(max_length=13)
    direccion = models.TextField()
    correo_electronico = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"