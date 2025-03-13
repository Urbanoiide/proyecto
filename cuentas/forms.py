# forms.py
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import re

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not re.match(r'^[a-zA-Z0-9]*$', username):
            raise ValidationError("El nombre de usuario solo puede contener letras y números.")
        if User.objects.filter(username=username).exists():
            raise ValidationError("Este nombre de usuario ya está en uso.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este correo electrónico ya está registrado.")
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres.")
        if not any(char.isdigit() for char in password1):
            raise ValidationError("La contraseña debe contener al menos un número.")
        if not any(char.isupper() for char in password1):
            raise ValidationError("La contraseña debe contener al menos una letra mayúscula.")
        if not any(char.islower() for char in password1):
            raise ValidationError("La contraseña debe contener al menos una letra minúscula.")
        return password1
