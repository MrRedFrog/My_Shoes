from django.db import models

class Usuario(models.Model):
    rut = models.CharField(max_length=12, unique=True, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    edad = models.IntegerField()
    celular = models.CharField(max_length=15)
    email = models.EmailField(max_length=50, unique=True)
    contraseña = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"
