from django.shortcuts import render

# Create your views here.

def index(request):
    """
    Funcion de vista index
    """
    
    return render(request, "index.html")

def create_user(request):
    """
    Funcion de vista create_user
    """
    
    # Obteniendo los valores de los formularios
    request.session['name'] = request.POST['name']
    request.session['email'] = request.POST['email']

    
    return render(request, "show.html")
