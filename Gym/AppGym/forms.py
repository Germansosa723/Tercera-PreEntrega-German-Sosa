from django import forms

class EntrenadoresFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    tipo_de_profesor= forms.CharField(max_length=30)

class InscriptoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email= forms.EmailField()

class RutinasFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    ejercicios = forms.CharField(max_length=300)