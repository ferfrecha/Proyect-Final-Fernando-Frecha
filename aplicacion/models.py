from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Genero(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=140)
    
    class Meta:
        verbose_name = "Genero"
        verbose_name_plural = "Generos"
        ordering = ['nombre']
        
    def __str__(self):
        return f"{self.nombre}: {self.descripcion}"

class Director(models.Model):
    nombre = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    nacimiento = models.IntegerField()
    
    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Directores"
        ordering = ['nombre']
        
    def __str__(self):
        return f"{self.nombre} ({self.nacionalidad}), nacido el: {self.nacimiento}"

class Pelicula(models.Model):
    titulo = models.CharField(max_length=50)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    duracion = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    ano = models.IntegerField()
    class Meta:
        verbose_name = "Pelicula"
        verbose_name_plural = "Peliculas"
        ordering = ['ano']
    def __str__(self):
        return f"{self.titulo} ({self.ano}) - {self.genero.nombre} - Dirigida por {self.director.nombre}"


class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def str(self):
        return f"{self.user} {self.imagen}"