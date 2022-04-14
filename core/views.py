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
        'logado': teste,
        'produtos': produtos,
        'introducao': 'É um framework Web Python de alto nível facilita o desenvolvimento de sites seguros.',
        'free': 'É gratuito e de código aberto, tem uma comunidade próspera e ativa.',
        'doc': 'Ótima documentação e muitas opções de suporte gratuito e pago.',
        'vantagem1': 'É seguro, expansível, flexível.',
        'vantagem2': 'É fácil de usar, rápido e simples, ampla documentação, design focado no uso.'
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
