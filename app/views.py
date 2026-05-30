from django.shortcuts import render

def inicio(request):
    return render(request,  'app/inicio.html')

def elenco(request):
    return render(request,  'app/elenco.html')

def sobre(request):
    return render(request,  'app/sobre.html')

#def usuarios(request):

    # lista_usuarios = [
    #     {
    #         "nome": "Ana Jéssica", 
    #         "matrícula": "20241181110010",
    #         "idade": 18,
    #         "cidade": "Ruy Barbosa"
    #     },
    #        {
    #         "nome": "Nathalia Mileni", 
    #         "matrícula": "20241181110011",
    #         "idade": 16,
    #         "cidade": "São Pedro"
    #     },
    #        {
    #         "nome": "Bruno Rafael", 
    #         "matrícula": "20241181110012",
    #         "idade": 20,
    #         "cidade": "São Tomé"
    #     },
    #         {
    #         "nome": "Danielly Rodrigues", 
    #         "matrícula": "20241181110013",
    #         "idade": 18,
    #         "cidade": "Barcelona"
    #     },
    #         {
    #         "nome": "Hermerson Daniel", 
    #         "matrícula": "20241181110014",
    #         "idade": 25,
    #         "cidade": "Barcelona"
    #     }
    # ]

    # context = {
    #     "usuarios": lista_usuarios,
    # }

    # return render(request, "meuapp/usuarios.html", context)
