from django.shortcuts import render

def inicio(request):
    return render(request,  'app/inicio.html')

def sobre(request):
    return render(request,  'app/sobre.html')

def elenco(request):
    
    lista_elenco = [
        {
            "foto": "damon.png",
            "nome": "Damon Salvatore", 
            "idade": 25,
            "função": "Protagonista",
            "local_nasc": "Mystic Falls, Virgínia"
        },
            {
            "foto": "stefan.png",
            "nome": "Stefan Salvatore", 
            "idade": 17,
            "função": "Protagonista",
            "local_nasc": "Mystic Falls, Virgínia"
        },
            {
            "foto": "elena.png",
            "nome": "Elena Gilbert", 
            "idade": 17,
            "função": "Protagonista",
            "local_nasc": "Mystic Falls, Virgínia"
        },
            {
            "foto": "caroline.png",
            "nome": "Caroline Forbes", 
            "idade": 17,
            "função": "Antagonista",
            "local_nasc": "Mystic Falls, Virgínia"
        },
            {
            "foto": "bonnie.png",
            "nome": "Bonnie Bennett", 
            "idade": 16,
            "função": "Antagonista",
            "local_nasc": "Mystic Falls, Virgínia"
        },
            {
            "foto": "jeremy.png",
            "nome": "Jeremy Gilbert", 
            "idade": 15,
            "função": "Antagonista",
            "local_nasc": "Mystic Falls, Virgínia"
        },
            {
            "foto": "alaric.png",
            "nome": "Alaric Saltzman", 
            "idade": 50,
            "função": "Antagonista",
            "local_nasc": "Boston, Massachusetts"
        },
            {
            "foto": "tyler.png",
            "nome": "Tyler Lockwood", 
            "idade": 16,
            "função": "Antagonista",
            "local_nasc": "Mystic Falls, Virgínia "
        },
            {
            "foto": "katherine.png",
            "nome": "Katherine Pierce", 
            "idade": 18,
            "função": "Antagonista",
            "local_nasc": "Bulgária"
        },
            {
            "foto": "klaus.png",
            "nome": "Klaus Mikaelson", 
            "idade": 20,
            "função": "Antagonista",
            "local_nasc": "Mystic Falls, Virgínia"
        },
            {
            "foto": "jenna.png",
            "nome": "Jenna Sommers", 
            "idade": 29,
            "função": "Antagonista",
            "local_nasc": "Mystic Falls, Virgínia"
        }
    ]

    context = {
    "personagens": lista_elenco,
    }

    return render(request, "app/elenco.html", context)
