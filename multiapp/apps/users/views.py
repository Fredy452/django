from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def register(request):
    """
    Funcion de vista register
    """
    return HttpResponse("marcador de posición para que los usuarios creen un nuevo registro de usuario")  # noqa: E501


def login(request):
    """
    Funcion de vista login user
    """
    
    return HttpResponse("marcador de posición para que los usuarios inicien sesión")  # noqa: E501

def index(request):
    """
    Funcion de vista index
    """
    return HttpResponse("Marcador de posición para luego mostrar toda la lista de usuarios")   # noqa: E501