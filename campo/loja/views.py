from django.shortcuts import render

def pesquisar(request):
    return render(request, 'loja/pesquisar.html',{})

#def cadastrar(request):
 #   print("chegou no cadastrar")
