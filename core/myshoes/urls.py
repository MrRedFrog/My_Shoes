from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario', views.indexFormulario, name= 'indexFormulario'),
    path('login', views.SessionFormulario, name= 'SessionFormulario'),
    path('nike', views.nike, name= 'nike'),
    path('adidas', views.adidas, name= 'adidas'),
    path('puma', views.adidas, name= 'puma')

]