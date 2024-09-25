from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # Añade related_name únicos para evitar conflictos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )