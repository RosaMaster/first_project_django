from django.shortcuts import render

from .models import Produto


def index(request):
    produtos = Produto.objects.all()
    print(dir(request))
    print(f"User: {request.user.last_name}")

    if str(request.user) == 'AnonymousUser':
        teste = 'Usuário não logado'
    else:
        teste = 'Usuário Logado'
    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é muito bom !!!',
        'logado': teste,
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    prod = Produto.objects.get(id=pk)

    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)
