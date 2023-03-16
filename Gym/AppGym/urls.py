from django.urls import path
from AppGym import views 

urlpatterns = [
    path('', views.inicio, name="Inicio"), 
    path('entrenadores/', views.entrenadores, name="Entrenadores"),
    path('inscriptos/', views.inscriptos, name="Inscriptos"),
    path('rutinas/', views.rutinas, name="Rutinas"),
   # path('entrenadoresFormulario', views.entrenadoresFormulario, name = 'entrenadoresFormulario'),
   # path('inscriptosFormulario', views.inscriptosFormulario, name = 'inscriptosFormulario'),
   # path('rutinasFormulario', views.rutinasFormulario, name = 'rutinasFormulario'),
]