from django.db import models
from django.contrib.auth.models import User 
from django.utils.translation import gettext_lazy as _

class Rol(models.TextChoices):
    ADMINISTRADOR = 'ADMINISTRADOR', _('administrador')
    productor = 'productor', _('productor') # Cambiado a 'Productor' según tu select
    cliente = 'cliente', _('cliente')
    TRANSPORTISTA = 'TRANSPORTISTA', _('Transportista')
    CONSULTOR = 'CONSULTOR', _('Consultor')


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    rol = models.CharField(
        max_length=20,
        choices=Rol.choices,
        default=Rol.cliente,
        verbose_name='Rol del usuario'
    )

    def __str__(self):
        return f'{self.usuario.username} - {self.rol}'
    

class Fruta(models.Model):
    nombre=models.CharField(max_length=300)
    descripcion=models.TextField()
    precio=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    #imagen=models.ImageField()
    marca=models.CharField(max_length=300)

    def __str__(self):
        return self.nombre