# aplicacion/forms.py
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Rol

class RegistroForm(UserCreationForm):
    # Añadimos el campo email requerido
    email = forms.EmailField(
        required=True,
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={'placeholder': 'correo@ejemplo.com', 'class': 'form-control'})
    )
    
    # Campo Rol (usamos los choices del modelo)
    rolReg = forms.ChoiceField(
        choices=Rol.choices,
        required=True,
        label='Rol',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    # Campo Nombre Completo (es opcional ya que no está en el modelo User)
    nombre = forms.CharField(
        required=False,
        label='Nombre Completo',
        widget=forms.TextInput(attrs={'placeholder': 'Ej: Juan Pérez', 'class': 'form-control'})
    )
    
    class Meta(UserCreationForm.Meta):
        # Aseguramos que el campo 'password2' esté incluido para la confirmación
        fields = UserCreationForm.Meta.fields + ('email', 'rolReg', 'nombre')
        
        # Aplicamos estilos de Bootstrap a los campos por defecto
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Ingrese un usuario', 'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Cree una contraseña', 'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirme su contraseña', 'class': 'form-control'}),
        }