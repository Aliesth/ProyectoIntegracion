from django.shortcuts import render, redirect
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction 
# Asegúrate de que tu modelo se llama 'Perfil' y está importado
from .models import Perfil # Importamos tu modelo Perfil
# Asegúrate de que tu modelo se llama 'Perfil' y está importado
from .models import Perfil, Rol # Importamos tu modelo Perfil
# Create your views here.
def registrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        user_email = request.POST.get('email')
        user_rol = request.POST.get('rolReg')
        
        # 💡 Imprime el Rol recibido para la depuración
        # print(f"--- DEPURACIÓN: Rol recibido: {user_rol} ---")
        
        if form.is_valid():
            
            # 1. Validación de rol: CRÍTICO para que no falle Perfil.objects.create
            if user_rol not in Rol.values:
                form.add_error(None, f"El rol '{user_rol}' no es una opción válida.")
                return render(request, 'login.html', {'form': form})
            
            try:
                with transaction.atomic():
                    # 2. Guardar el objeto User (contraseña y username)
                    user = form.save(commit=False)
                    user.email = user_email
                    user.save() 
                    
                    # 3. Crear el objeto Perfil con el rol
                    Perfil.objects.create(usuario=user, rol=user_rol)

                    # 4. Iniciar sesión y redirigir
                    login(request, user)
                    return redirect('index')
            
            except Exception as e:
                # 📢 ¡CRÍTICO! IMPRIME ESTO EN LA TERMINAL 📢
                print("=============================================")
                print(f"🛑 FALLO DE TRANSACCIÓN: El usuario NO se guardó.")
                print(f"🛑 RAZÓN DEL FALLO: {e}")
                print("=============================================")
                
        # Si la validación falla (ej: contraseñas no coinciden) o hay un error en la BD
        return render(request, 'login.html', {'form': form})
        
    else:
        # Petición GET
        form = UserCreationForm()
        return render(request, 'login.html', {'form': form})

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