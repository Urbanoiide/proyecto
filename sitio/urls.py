"""
URL configuration for sitio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from ejemplo.views import hola_mundo
from libro.views import lista_libros
from myapp.views import index
from django.shortcuts import redirect
from app_kolb.views import cuestionario, resultados
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),  # Redirige la raíz al login),
    path('app', include('app_kolb.urls')),
    path('hola/', hola_mundo),
    path('libros/', lista_libros, name='lista_libros'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cuentas/', include('cuentas.urls')),
]
