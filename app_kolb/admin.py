# app_kolb/admin.py
from django.contrib import admin
from .models import Pregunta, Respuesta # Importa el modelo

admin.site.register(Pregunta)

admin.site.register(Respuesta)   # Registra el modelo en el admin