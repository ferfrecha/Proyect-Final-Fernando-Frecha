
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', home, name="home" ),
    path('directores/', directores, name="directores" ),
    path('generos/', generos, name="generos" ),
    path('peliculas/', peliculas, name="peliculas" ),
    
    path('pelicula_form/', pelicula_form, name="pelicula_form" ),
    path('genero_form/', genero_form, name="genero_form" ),
    path('director_form/', director_form, name="director_form" ),
    
    
    path('buscar_form/', buscarpelicula, name="buscarpelicula" ),
    path('buscar/', buscar, name="buscar" ),
    
    path('contact/', contact, name="contact" ),
    ]
