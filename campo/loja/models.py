from django.db import models
from django.utils import timezone


class Produto (models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    valor = models.IntegerField()
    valores = models.IntegerField()
    validade = models.DateTimeField(default = timezone.now)
    estoque = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Dados_usuario (models.Model):
    rua = models.CharField(max_length=200)
    numero = models.IntegerField()
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome



class Fornecedor (models.Model):
    nome = models.CharField(max_length=200)
    cnpj = models.IntegerField()

    def __str__(self):
        return self.nome