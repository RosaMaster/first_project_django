from django.shortcuts import render


def index(request):
    print(dir(request))
    print(f"User: {request.user.last_name}")

    if str(request.user) == 'AnonymousUser':
        teste = 'Usuário não logado'
    else:
        teste = 'Usuário Logado'
    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é muito bom !!!',
        'logado': teste
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')
