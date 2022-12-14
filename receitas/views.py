from django.shortcuts import render, get_object_or_404
from .models import Receita

def index(request):
    receitas = Receita.objects.order_by('-id').filter(publicada=True)
    dados = {
        'receitas': receitas
    }

    return render(request, 'index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_exibida = {
        'receita': receita
    }

    return render(request, 'receita.html', receita_exibida)

def buscar(request):
    receitas = Receita.objects.order_by('-id').filter(publicada=True)
    if 'buscar' in request.GET:
        nome_buscar = request.GET['buscar']
        if buscar:
            receitas = receitas.filter(nome_receita__icontains=nome_buscar)

    dados = {
        'receitas': receitas
    }

    return render(request, 'buscar.html', dados)