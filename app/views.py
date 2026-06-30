from django.shortcuts import render
from .models import Elenco

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
    
    lista_sobre = [
                {
                "titulo_resumo": "Resumo da série",
                "resumo": "Diários de um Vampiro (The Vampire Diaries) é uma série de drama sobrenatural centrada em Elena Gilbert, uma adolescente que se apaixona por Stefan Salvatore, um vampiro centenário. O retorno do irmão de Stefan, o perigoso e impulsivo Damon, inicia um clássico triângulo amoroso e revela os segredos sombrios de Mystic Falls",
                "titulo_sobre": "Sobre o site",
                "sobre": "Este espaço foi criado para reunir informações sobre uma das séries sobrenaturais mais conhecidas da televisão. Aqui, você poderá conhecer melhor os personagens e  descobrir mais sobre o universo de Mystic Falls.", 
                "imagem": "vampire.jpg",
                "titulo_autores": "Autores",
                "autores": "Este site foi desenvolvido por: Emilly Laviny e Araújo Somos estudantes e desenvolvemos este projeto com dedicação, criatividade e interesse pela série, unindo conhecimentos de desenvolvimento web e design."
            }
        ]

    context = {
        "informacoes": lista_sobre,
    }

    return render(request, "app/sobre.html", context)

