# from http.client import HTTPResponse
from socket import htons
from django.shortcuts import render
from django.http import HttpResponse
from .models import curso

# Create your views here.

def crear_curso(request, camada):
    Curso= curso(nombre='Python', camada= camada)
    Curso.save()

    return HttpResponse (f'Curso creado {camada}')

def inicio(request):
    return render(request, 'AppCoder/inicio.html') # luego de esto tengo que ir a settings y agregar la dir de los templates
    # return HttpResponse ('inicio')

def cursos(request):
    return HttpResponse ('curso')  

def profesores(request):
    return render(request, 'AppCoder/profesores.html')
    #return HttpResponse ('profesores')

def estudiantes(request):
    return HttpResponse ('estudiantes')

def entregables(request):
    return HttpResponse ('entregables')