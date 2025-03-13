# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm

def registro(request):
    """Vista para el registro de usuarios."""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Crea el usuario sin guardar todavía
            user.is_staff = False           # El usuario no será staff ni superusuario
            user.is_superuser = False
            user.save()                     # Guarda al usuario en la base de datos
            login(request, user)            # Inicia sesión automáticamente
            messages.success(request, f'¡Registro exitoso! Bienvenido, {user.username}')
            return redirect('login')        # Redirige al login o a otra página
        else:
            messages.error(request, 'Corrige los errores del formulario.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})
