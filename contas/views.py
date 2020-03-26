from django.shortcuts import render, redirect
from .models import Transacao
from .form import TransacaoForm
import datetime

def home(request):

    data = dict()
    data['transacoes'] = ['t1', 't2', 't3']
    data['now'] = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'contas/home.html', data)

def Listagem(request):

    data = dict()
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)


def nova_transacao(request):

    data = dict()
    form = TransacaoForm(request.POST or None)

    if form.is_valid():

        form.save()
        return redirect('url_listagem')

    data['form'] = form

    return render(request, 'contas/form.html', data)

def update(request, pk):

    data = dict()
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():

        form.save()
        return redirect('url_listagem')

    data['form'] = form
    data['transacao'] = transacao

    return render(request, 'contas/form.html', data)

def delete(request, pk):

    data = dict()
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')

# Create your views here.
