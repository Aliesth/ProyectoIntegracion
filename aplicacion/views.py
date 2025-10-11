from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.db import transaction
from django.contrib.auth.models import Group

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


def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST) 
        
        if form.is_valid():
            user_rol_name = form.cleaned_data.get('rolReg')
            
            # --- INICIO DE LA TRANSACCIÓN ATÓMICA ---
            try:
                with transaction.atomic():
                    # 1. Guarda el objeto User
                    user = form.save() 
                    
                    # 2. Crea el objeto Perfil
                    Perfil.objects.create(usuario=user, rol=user_rol_name)

                    # 3. 🎯 LÓGICA DE ASIGNACIÓN DE GRUPO (CORREGIDA) 🎯
                    try:
                        # Busca el Grupo de Django
                        grupo_django = Group.objects.get(name=user_rol_name)
                        user.groups.add(grupo_django)
                        print(f"✅ Usuario {user.username} asignado al grupo {user_rol_name}.")
                        
                    except Group.DoesNotExist:
                        # Si el grupo no existe, solo lo reportamos pero no revertimos el registro
                        print(f"🛑 ADVERTENCIA: El Grupo '{user_rol_name}' no existe en Django. Asignación omitida.")
                        pass 
                    
                    # 4. Inicia sesión y redirige (Solo si todo lo anterior tuvo éxito)
                    login(request, user)
                    return redirect('index')  # Es mejor redirigir al 'index' (dashboard)
                
            except Exception as e:
                # Si falla cualquier cosa dentro de la transacción, se revierte.
                print(f"🛑 FALLO CRÍTICO DURANTE LA TRANSACCIÓN: {e}")
                form.add_error(None, "Ocurrió un error al crear el usuario. Por favor, inténtelo de nuevo.")
                
        # Si la validación de formulario o la transacción falla
        return render(request, 'login.html', {
            'register_form': form, # Contiene los errores de registro
            'login_form': AuthenticationForm() 
        })
        
    else:
        # Petición GET
        # Asumiendo que 'login_usuario' es el nombre de la URL para la vista de login.
        return redirect('login_usuario')
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