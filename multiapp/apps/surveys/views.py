from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """
    Funcion de vista index
    """
    return HttpResponse("marcador de posición para mostrar todas las encuestas creadas")


def new(request):
    """
    Funcion de vista new survey
    """
    
    return HttpResponse("marcador de posición para que los usuarios agreguen una nueva encuesta")  # noqa: E501