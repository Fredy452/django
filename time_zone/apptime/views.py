from django.shortcuts import render
from datetime import datetime

# Create your views here.

def index(request):
    """
    Funcion de vista index
    """
    current_time = datetime.now()
    formatted_time = current_time.strftime("%d %b, %Y %I:%M:%S %p")
    
    context = {
        "time": formatted_time
    }
    return render(request, 'index.html', context)
