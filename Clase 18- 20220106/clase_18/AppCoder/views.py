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