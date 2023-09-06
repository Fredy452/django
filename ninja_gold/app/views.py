
from django.shortcuts import render

import random 
from datetime import datetime 

# Create your views here.

def index(request):
    """
    Funcion de vista index
    """
    
    return render(request, 'index.html')

def money(request, activity):
    if 'farm' not in request.session:
        request.session['farm'] = 0
    
    if 'cave' not in request.session:
        request.session['cave'] = 0

    if 'house' not in request.session:
        request.session['house'] = 0
        
    if 'casino' not in request.session:
        request.session['casino'] = 0
    
    messages = request.session.get('messages', [])
    info = "text-info"
    date = datetime.now()
    formatted_date = date.strftime("%d %b %Y %H:%M:%S")
    
    if activity == 'farm':
        gold_earned = random.randint(10, 20)
        request.session['farm'] += gold_earned
        messages.append(f"Ganaste {gold_earned} de oro en la granja {formatted_date}")
    
    if activity == 'cave':
        gold_earned = random.randint(5, 10)
        request.session['cave'] += gold_earned
        messages.append(f"Ganaste {gold_earned} de oro en la mina {formatted_date}")
    
    if activity == 'house':
        gold_earned = random.randint(2, 5)
        request.session['house'] += gold_earned
        messages.append(f"Ganaste {gold_earned} de oro en house {formatted_date}")
        
    if activity == 'casino':
        gold_earned = random.randint(-50, 50)
        request.session['casino'] += gold_earned
        
        if gold_earned >0:
            messages.append(f"Ganaste {gold_earned} de oro en el casino {formatted_date}")  # noqa: E501
        else:
            messages.append(f"Perdiste {gold_earned} de oro el casino {formatted_date}")
            info = "text-danger"
    
    # Calcula el nuevo total sumando las ganancias de todas las actividades
    total = sum([request.session.get(activity, 0) for activity in ['farm',
                'cave', 'house']])
    
    # Agrega el nuevo total a la sesión
    request.session['total'] = total
    
    # Cambiamnos el orden de messages
    messages = list(reversed(messages))
    
    context = {
        "messages": messages,
        "info": info,
        "total": total,
    }

    request.session['messages'] = messages
    
    return render(request, 'index.html', context)
