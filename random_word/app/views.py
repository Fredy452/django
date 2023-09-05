from django.shortcuts import render
from faker import Faker

# Instancia de Faker
fake = Faker()

# Create your views here.
def random_word(request):
    """
    Funcion de vista random_word
    """
    return render(request, "index.html")


def word(request):
    """
    Funcion de vista random_word
    """
    random_word = fake.word()

    if 'contador' in request.session:
        request.session['contador'] += 1
    else:
        request.session['contador'] = 0
    
    context = {
        "word": random_word,
        "contador": request.session['contador']
    }
    
    return render(request, "index.html", context)


def reset(request):
    """
    Funcion de vista random_reset
    """
    request.session.clear()
    return render(request, "index.html")