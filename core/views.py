from django.shortcuts import render

from core.models import Produto


def index(request):
    produtos = Produto.objects.all()
    context = {
        'curso': 'Programação WEB com Django Framework',
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, id):
    p = Produto.objects.filter(id=id).first()
    return render(request, 'produto.html', context={
        'produto': p
    })
