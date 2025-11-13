from django.shortcuts import render, redirect
from .models import Oracao, RelacaoCoordenativa, Conector


def index(request):
    relacoes = RelacaoCoordenativa.objects.all().order_by('-id')
    return render(request, 'coordenacoes/index.html', {'relacoes': relacoes})

def criar_oracao(request):
    if request.method == 'POST':
        texto = request.POST.get('texto')
        if texto:
            Oracao.objects.create(texto=texto)
            return redirect('index')
    return render(request, 'coordenacoes/oracao_form.html')

def criar_relacao(request):
    oracoes = Oracao.objects.all()
    conectores = Conector.objects.all()

    if request.method == 'POST':
        oracao_1_id = request.POST.get('oracao_1')
        oracao_2_id = request.POST.get('oracao_2')
        conector_id = request.POST.get('conector')
        observacoes = request.POST.get('observacoes', '')

        RelacaoCoordenativa.objects.create(
            oracao_1_id=oracao_1_id,
            oracao_2_id=oracao_2_id,
            conector_id=conector_id,
            observacoes=observacoes
        )
        return redirect('index')

    return render(request, 'coordenacoes/relacao_form.html', {
        'oracoes': oracoes,
        'conectores': conectores
    })
