from django.urls import path
from . import views

urlpatterns = [
    path('', views.cuestionario, name='cuestionario'),
    path('resultados/<int:id>/', views.resultados, name='resultados'),
]