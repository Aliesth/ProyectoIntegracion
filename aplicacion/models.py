from django.db import models
from django.contrib.auth.models import User 
from django.utils.translation import gettext_lazy as _

class Rol(models.TextChoices):
    ADMINISTRADOR = 'ADMINISTRADOR', _('Administrador')
    EMPLEADO = 'EMPLEADO', _('Empleado') # El valor que se guarda es EMPLEADO
    CLIENTE = 'CLIENTE', _('Cliente')
    TRANSPORTISTA = 'TRANSPORTISTA', _('Transportista')
    CONSULTOR = 'CONSULTOR', _('Consultor')


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    rol = models.CharField(
        max_length=20,
        choices=Rol.choices,
        default=Rol.CLIENTE,
        verbose_name='Rol del usuario'
    )

    def __str__(self):
        return f'{self.usuario.username} - {self.rol}'