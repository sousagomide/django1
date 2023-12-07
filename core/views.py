from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

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
    #p = Produto.objects.filter(id=id).first()
    p = get_object_or_404(Produto, id=id)
    return render(request, 'produto.html', context={
        'produto': p
    })

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)