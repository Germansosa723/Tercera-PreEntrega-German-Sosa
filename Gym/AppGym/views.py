from django.shortcuts import render

# Create your views here.

def inicio(request):
      return render(request, "inicio.html")

def entrenadores(request):
      return render(request, "entrenadores.html")

def inscriptos(request):
      return render(request, "inscriptos.html")

def rutinas(request):
      return render(request, "rutinas.html")