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

