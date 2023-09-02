from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

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
    
    
    path('modifPelicula/<id_pelicula>/', modifPelicula, name="modifPelicula"),
    
    path('deletePelicula/<id_pelicula>/', deletePelicula, name="deletePelicula"),
    
    
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
    path('registro/', register, name="registro"),
    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
    
    
    ]
