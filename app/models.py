from django.db import models

class Elenco(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.CharField(max_length=5)
    funcao = models.CharField(max_length=50)
    local_nasc = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome