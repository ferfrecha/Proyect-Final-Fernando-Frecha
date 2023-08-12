
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', home, name="home" ),
    path('directores/', directores, name="directores" ),
    path('generos/', generos, name="generos" ),
    path('peliculas/', peliculas, name="peliculas" ),
    ]
