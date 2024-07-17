from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name= 'register'),
    path('login/', views.login, name= 'login'),
    path('nike/', views.nike, name= 'nike'),
    path('adidas/', views.adidas, name= 'adidas'),
    path('puma/', views.adidas, name= 'puma'),
    path('guardar_usuario/', views.guardar_usuario, name='guardar_usuario'),  # Ruta para guardar un nuevo usuario,
    path('guardar_categoria/', views.guardar_categoria, name='guardar_categoria') # Ruta para guardar una nueva categoria,

]
