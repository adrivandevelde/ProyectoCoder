from django.urls import path
from AppCoder.views import crear_curso, inicio, profesores

urlpatterns = [
    path('crearcurso/<camada>', crear_curso),
    path('', inicio),
    path('profesores', profesores),
]