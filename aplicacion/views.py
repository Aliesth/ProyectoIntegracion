from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.db import transaction

from .models import Perfil 
from .forms import RegistroForm # <-- Importamos el formulario personalizado

# Vista Principal/Dashboard
def index(request):
    # Aquí puedes añadir lógica de require login, por ahora solo renderiza
    return render(request, 'index.html') 


# VISTA DE LOGIN (Maneja el inicio de sesión)
def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('index') # Éxito: Va a /home/

        # FALLO: Si la validación falla o authenticate devuelve None
        return render(request, 'login.html', {
            'login_form': form, # Contiene los errores de autenticación
            'register_form': RegistroForm() 
        })

    else:
        # Petición GET: Muestra la página de Login/Registro
        return render(request, 'login.html', {
            'login_form': AuthenticationForm(), 
            'register_form': RegistroForm()
        })


# VISTA DE REGISTRO (Maneja la creación de cuenta)
def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST) 
        
        if form.is_valid():
            user_rol = form.cleaned_data.get('rolReg')
            
            try:
                with transaction.atomic():
                    # CRÍTICO: form.save() guarda el objeto User completo con email y contraseña hasheada
                    user = form.save() 
                    
                    # Crea el objeto Perfil
                    Perfil.objects.create(usuario=user, rol=user_rol)

                    # Inicia sesión y redirige
                    login(request, user)
                    return redirect('login') 
            
            except Exception as e:
                # Si falla aquí, la causa está en la BD (ej. migraciones o restricción de campo)
                print(f"🛑 FALLO CRÍTICO DE GUARDADO EN BD: {e}")
                form.add_error(None, "Ocurrió un error al crear el usuario. Por favor, inténtelo de nuevo.")
                
        # Si la validación de formulario (ej. contraseñas) o la transacción falla
        return render(request, 'login.html', {
            'register_form': form, # Contiene los errores de registro
            'login_form': AuthenticationForm() 
        })
        
    else:
        # Petición GET (Esto solo se usa si acceden directamente a /register/, pero lo mejor es redirigir a login)
        return redirect('login') 
# Nota: También necesitas una vista simple para 'index'
def index(request):
    return render(request, 'index.html') 

def index(request):
    return render(request, 'index.html')

def productos(request):
    return render(request, 'productos.html')

def carrito(request):
    return render(request, 'carrito.html')

def subastas(request):
    return render(request, 'subastas.html')

def reportes(request):
    return render(request, 'reportes.html')

def ventas(request):
    return render(request, 'ventas.html')

def nosotros(request):
    return render(request, 'nosotros.html')