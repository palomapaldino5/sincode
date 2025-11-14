from django.shortcuts import render, redirect
from .models import UnidadeCoordenada, ConectorCoordenativo, RelacaoCoordenativa


def index(request):
    relacoes = RelacaoCoordenativa.objects.all().order_by('-id')
    return render(request, 'coordenacoes/index.html', {'relacoes': relacoes})


def criar_unidade(request):
    if request.method == 'POST':
        texto = request.POST.get('texto')
        if texto:
            UnidadeCoordenada.objects.create(texto=texto)
            return redirect('index')

    return render(request, 'coordenacoes/unidade_form.html')


def criar_relacao(request):
    unidades = UnidadeCoordenada.objects.all()
    conectores = ConectorCoordenativo.objects.all()

    if request.method == 'POST':
        u1 = request.POST.get('unidade_1')
        u2 = request.POST.get('unidade_2')
        conector = request.POST.get('conector')
        obs = request.POST.get('observacoes', '')

        RelacaoCoordenativa.objects.create(
            unidade_1_id=u1,
            unidade_2_id=u2,
            conector_id=conector,
            observacoes=obs
        )
        return redirect('index')

    return render(request, 'coordenacoes/relacao_form.html', {
        'unidades': unidades,
        'conectores': conectores
    })
