from django.db import models

class Elenco(models.Model):
    imagem = models.ImageField(upload_to='assets/')
    nome = models.CharField(max_length=50)
    idade = models.CharField(max_length=5)
    funcao = models.CharField(max_length=50)
    local_nasc = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

class Sobre(models.Model):
    titulo_resumo = models.CharField(max_length=50)
    resumo = models.TextField(max_length=200)
    titulo_sobre = models.CharField(max_length=50)
    sobre = models.TextField(max_length=200)
    imagem = models.ImageField(upload_to='assets/')
    titulo_autores = models.CharField(max_length=50)
    autores = models.TextField(max_length=200)

    def __str__(self):
        return self.nome
