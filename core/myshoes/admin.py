from django.contrib import admin
from .models import Usuario, Categoria, Producto

# Registra el modelo Usuario
admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Producto)