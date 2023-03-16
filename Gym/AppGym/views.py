from django.http import HttpResponse
from django.shortcuts import render
from AppGym.models import Entrenadores, Inscriptos, Rutinas
from AppGym.forms import EntrenadoresFormulario, InscriptoFormulario, RutinasFormulario

# Create your views here.

def inicio(request):
      return render(request, "inicio.html")

def entrenadores(request):
      return render(request, "entrenadores.html")

def inscriptos(request):
      return render(request, "inscriptos.html")

def rutinas(request):
      return render(request, "rutinas.html")

def entrenadores(request):

      if request.method == 'POST':

            miFormulario = EntrenadoresFormulario(request.POST) 

            print(miFormulario)

            if miFormulario.is_valid:   

                  informacion = miFormulario.cleaned_data

                  curso = Entrenadores (nombre=informacion['entrenadores'], apellido=informacion['apellido'], email=informacion['email'], tipo_de_profesor=informacion['tipo de profesor']) 

                  curso.save()

                  return render(request, "inicio.html") 

      else: 

            miFormulario= EntrenadoresFormulario() 

      return render(request, "entrenadores.html", {"miFormulario":miFormulario})


def inscriptos(request):

      if request.method == 'POST':

            miFormulario = InscriptoFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:   

                  informacion = miFormulario.cleaned_data

                  inscriptos = Inscriptos(nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'],) 

                  inscriptos.save()

                  return render(request, "inicio.html") 

      else: 

            miFormulario= InscriptoFormulario() 

      return render(request, "inscriptos.html", {"miFormulario":miFormulario})

def Buscar(request):

      if  request.GET["rutinas"]:
	      
            rutinas = request.GET['rutinas'] 
            rutinas = Rutinas.objects.filter(rutinas__icontains=rutinas)

            return render(request, "inicio.html", {"rutinas":rutinas, "rutinas":rutinas})

      else: 

	      respuesta = "pecho,espalda,biceps,triceps,piernas y hombro"
                  
