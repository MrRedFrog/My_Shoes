from django.shortcuts import render

# Create your views here.

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

