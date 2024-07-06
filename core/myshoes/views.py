from django.shortcuts import render

# Create your views here.

def index (request): 
    return render(request, 'index.html')

def indexFormulario (request):
    return render(request, 'indexformulario.html')

def SessionFormulario (request):
    return render (request, 'SessionFormulario.html')

def nike (request):
    return render (request, 'nike.html')

def adidas (request):
    return render (request, 'adidas.html')

def puma (request):
    return render (request, 'puma.html')

