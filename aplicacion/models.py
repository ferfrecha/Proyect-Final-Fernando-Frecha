from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=140)
    
    def __str__(self):
        return f"{self.nombre}: {self.descripcion}"

class Director(models.Model):
    nombre = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    nacimiento = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} ({self.nacionalidad}), nacido el: {self.nacimiento}"

class Pelicula(models.Model):
    titulo = models.CharField(max_length=50)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    duracion = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    ano = models.IntegerField()
    
    def __str__(self):
        return f"{self.titulo} ({self.ano}) - {self.genero} - Dirigida por {self.director}"
