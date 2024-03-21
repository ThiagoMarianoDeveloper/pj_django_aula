from django.db import models
from django.utils import timezone 

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.nome
