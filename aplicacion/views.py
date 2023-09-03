from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

from .forms import *
from django.urls import reverse_lazy

from django.views.generic import UpdateView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth       import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import *
from django.contrib.auth.decorators import permission_required

#from PIL import Image

from .models import Pelicula
from .forms import peliculaForm

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

@login_required
#@permission_required('')
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


@login_required
def modifPelicula(request, id_pelicula):
    generos = Genero.objects.all()
    directores = Director.objects.all()
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
        return redirect('peliculas')
    
    return render(request, "aplicacion/pelicula_form_modif.html", {"generos": generos, "directores": directores})


@login_required
#@permission_required('')
def deletePelicula(request, id_pelicula):
    pelicula = Pelicula.objects.get(id=id_pelicula)
    pelicula.delete()
    return redirect(reverse_lazy('peliculas'))



def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)

                try:
                    Avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar

                return render(request, "aplicacion/base.html", {'mensaje': f"Bienvenido {usuario}!"})
            else:
                return render(request, "aplicacion/base.html", {'form': miForm, 'mensaje': "Los datos son inválidos"})
        else:
            return render(request, "aplicacion/base.html", {'form': miForm, 'mensaje': "Los datos son inválidos"})

    miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": miForm})



def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)

        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = RegistroUsuariosForm()

    return render(request, "aplicacion/registro.html", {"form": miForm})

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, "aplicacion/base.html")
        else:
            return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario.username})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)

            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            avatar=Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request, "aplicacion/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregar_avatar.html", {'form': form})


