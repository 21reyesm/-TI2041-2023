from django.db import models
from django.contrib.auth.models import User

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Publicacion(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField(default="Sin contenido")
    etiquetas = models.ManyToManyField(Etiqueta)

    def __str__(self):
        return self.titulo

#admin0 admin123