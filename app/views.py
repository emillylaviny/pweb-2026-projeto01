from django.shortcuts import render
from .models import Elenco
from .models import Sobre

def inicio(request):
    return render(request,  'app/inicio.html')

def sobre(request):
    return render(request,  'app/sobre.html')

def elenco(request):
    
    elenco = Elenco.objects.all()

    context = {
        "elenco": elenco,
    }

    return render(request, "app/elenco.html", context)

def sobre(request):
    
    lista_sobre = Sobre.objects.all()
    
    context = {
        "informacoes": lista_sobre,
    }

    return render(request, "app/sobre.html", context)

