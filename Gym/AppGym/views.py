from django.shortcuts import render
from AppGym.models import Entrenadores, Inscriptos, rutinas

# Create your views here.

def inicio(request):
      return render(request, "inicio.html")

def entrenadores(request):
      return render(request, "entrenadores.html")

def inscriptos(request):
      return render(request, "inscriptos.html")

def rutinas(request):
      return render(request, "rutinas.html")

def entrenadoresFormulario(request):
      return render (request,"AppGym/entrenadoresFormulario.html")

def inscriptosFormulario(request):
      return render (request,"AppGym/inscriptosFormulario.html")

def rutinasFormulario(request):
      return render (request,"AppGym/rutinasFormulario.html")