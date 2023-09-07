from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    """
    Funcion de vista `ìndex`
    """

    return HttpResponse(
        "marcador de posición para luego mostrar una lista de todos los blogs con un método llamado")  # noqa: E501


def new(request):
    """
    Funcion de vista new
    """
    return HttpResponse("marcador de posición para mostrar un nuevo formulario para crear un nuevo blog")


def create(request):
    """
    Funcion de vista create, que redirije a index
    """

    return index(request)


def show(request, number):
    """
    Funcion de vista index
    """

    return HttpResponse(f"Marcador de posición para mostrar el número de blog: {number}")

def edit(request, number):
    """
    Editar
    """
    return HttpResponse(f"marcador de posición para editar el blog {number}")


def delete(request, number):
    """
    Delete
    """
    return index(request)