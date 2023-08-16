from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    return render(request, "aplicacion/home.html")

def peliculas(request):
    contexto = {'peliculas': Pelicula.objects.all()}
    return render(request, "aplicacion/peliculas.html", contexto)

def directores(request):
    contexto = {'directores': Director.objects.all() }
    return render(request, "aplicacion/directores.html", contexto)

def generos(request):
    contexto = {'generos': Genero.objects.all()}
    return render(request, "aplicacion/generos.html", contexto)

def pelicula_form(request):
    if request.method == "POST":
        genero_id = request.POST['genero']
        genero_instance = Genero.objects.get(pk=genero_id)
        
        director_id = request.POST['director']
        director_instance = Director.objects.get(pk=director_id)
        
        pelicula = Pelicula(
            titulo=request.POST['titulo'],
            genero=genero_instance,
            duracion=request.POST['duracion'],
            director=director_instance,
            ano=request.POST['ano'],
        )
        pelicula.save()
        return HttpResponse("Pelicula guardada con exito")
    
    generos = Genero.objects.all()
    directores = Director.objects.all()
    return render(request, "aplicacion/pelicula_form.html", {"generos": generos, "directores": directores})


def genero_form(request):
    if request.method == "POST":
        genero = Genero(nombre=request.POST['nombre'],
                            descripcion=request.POST['descripcion'],
                            )
        genero.save()
        return HttpResponse("Genero guardada con exito")   
    return render(request, "aplicacion/genero_form.html")  

def director_form(request):
    if request.method == "POST":
        director = Director(nombre=request.POST['nombre'],
                        nacionalidad=request.POST['nacionalidad'],
                        nacimiento=request.POST['nacimiento'],
                        )
        director.save()
        return HttpResponse("Director guardado con exito")   
    return render(request, "aplicacion/director_form.html")  


def buscarpelicula(request):
    return render(request, "aplicacion/buscar_form.html")

def buscar(request):
    if 'buscar' in request.GET:
        patron = request.GET['buscar']
        peliculas = Pelicula.objects.filter(titulo__icontains=patron) 
        contexto = {"peliculas": peliculas}
        return render(request, "aplicacion/peliculas.html", contexto)
    return HttpResponse("Búsqueda sin resultado")
    
    
def contact(request):
    return render(request, "aplicacion/contact.html")