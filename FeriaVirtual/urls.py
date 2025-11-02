"""
URL configuration for FeriaVirtual project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from aplicacion import views
from aplicacion.views import CatalogoFrutasView



app_nanme = 'aplicacion'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_usuario, name='login'), 
    # 2. La ruta de Registro (a donde apunta el action del formulario)
    path('register/', views.registrar_usuario, name='register'),
    # 3. La página de Inicio real (a donde redirige después del login exitoso)
    path('home/', views.index, name='index'), 
    path('productos/', views.productos, name='productos'),
    path('carrito/', views.carrito, name='carrito'),
    path('subastas/', views.subastas, name='subastas'),
    path('reportes/', views.reportes, name='reportes'),
    path('ventas/', views.ventas, name='ventas'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('catalogo/',CatalogoFrutasView.as_view() ,name='catalogo_frutas')
]