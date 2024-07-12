from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Usuario

# Create your views here.

def guardar_usuario(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')
        apellido_paterno = request.POST.get('apellido_paterno')
        apellido_materno = request.POST.get('apellido_materno')
        edad = request.POST.get('edad')
        celular = request.POST.get('celular')
        email = request.POST.get('email')
        contraseña = request.POST.get('contraseña')

        try:
            # Verificar si ya existe un usuario con el mismo email o rut
            if Usuario.objects.filter(email=email).exists() or Usuario.objects.filter(rut=rut).exists():
                messages.error(request, 'Ya existe un usuario con este email o rut')
                return render(request, 'register.html')

            # Crear el nuevo usuario
            usuario = Usuario.objects.create(
                rut=rut,
                nombre=nombre,
                apellido_paterno=apellido_paterno,
                apellido_materno=apellido_materno,
                edad=edad,
                celular=celular,
                email=email,
                contraseña=contraseña
            )

            # Redirigir a alguna página de éxito o realizar otra acción necesaria
            return redirect('index')  # Redirige al inicio u otra página

        except Exception as e:
            return HttpResponse(f"Error al guardar el usuario: {e}", status=500)

    return render(request, 'register.html')

def index (request): 
    return render(request, 'index.html')

def register (request):
    return render(request, 'register.html')

def login (request):
    return render (request, 'login.html')

def nike (request):
    return render (request, 'nike.html')

def adidas (request):
    return render (request, 'adidas.html')

def puma (request):
    return render (request, 'puma.html')

