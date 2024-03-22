from django.contrib import admin
from .models import Produto, Dados_usuario, Fornecedor

admin.site.register(Produto)
admin.site.register(Dados_usuario)
admin.site.register(Fornecedor)
