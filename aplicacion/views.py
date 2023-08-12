from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    return render(request, "aplicacion/home.html")

def peliculas(request):
    return render(request, "aplicacion/peliculas.html")

def directores(request):
    contexto = {'directores': Director.objects.all() }
    return render(request, "aplicacion/directores.html", contexto)

def generos(request):
    return render(request, "aplicacion/generos.html")