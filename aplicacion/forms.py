# aplicacion/forms.py
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Rol

class RegistroForm(UserCreationForm):
    # Añadimos el campo email aquí
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'correo@ejemplo.com'})
    )
    
    # Campo Rol para usar en la vista (es solo un campo del formulario, no del modelo User)
    rolReg = forms.ChoiceField(
        choices=Rol.choices,
        required=True
    )
    
    # Opcional: Nombre completo (si solo es informativo en el formulario)
    nombre = forms.CharField(required=False) 

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', 'rolReg')

# Nota: Si el campo 'email' ya está definido en el modelo User como único,
# esta forma garantiza que la validación se realice antes de la vista.