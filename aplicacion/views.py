from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request, 'login.html')

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