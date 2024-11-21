from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import Jogo
from .models import TabelaBrasileirao
from django.db.models import F
from .forms import TabelaBrasileiraoForm
from .forms import JogoForm
import logging
def jogos_view(request):
    jogos = Jogo.objects.all()  # Obtém todos os jogos armazenados no banco de dados

    if request.method == 'POST':
        form = JogoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados no banco de dados
            return redirect('jogos')  # Redireciona de volta para a página de jogos
    else:
        form = JogoForm()

    return render(request, 'jogos.html', {'jogos': jogos, 'form': form})

def visualizar_jogos(request):
    jogos = Jogo.objects.all()  # Obter todos os jogos cadastrados
    return render(request, 'visualizar_jogos.html', {'jogos': jogos})


def deletar_jogo(request, id):
    if request.method == 'DELETE':  # Verifica se é uma requisição DELETE
        try:
            jogo = Jogo.objects.get(id=id)  # Busca o jogo pelo ID
            jogo.delete()  # Exclui o jogo
            return JsonResponse({"message": "Jogo excluído com sucesso."}, status=200)
        except Jogo.DoesNotExist:
            return JsonResponse({"error": "Jogo não encontrado."}, status=404)
    return HttpResponseNotAllowed(['DELETE'])


def cadastrar_tabela(request):
    if request.method == "POST":
        forms = []
        for i in range(1, 21):  # Gerar múltiplos formulários
            form = TabelaBrasileiraoForm(request.POST, prefix=f'time_{i}')
            if form.is_valid():
                forms.append(form)
            else:
                print(f"Erro no formulário {i}: {form.errors}")

        if forms:
            try:
                for form in forms:
                    form.save()  # Tenta salvar o formulário
                return redirect('mostrar_tabela')  # Redireciona para a página de exibição da tabela
            except Exception as e:
                print(f"Erro ao salvar os dados: {e}")  # Captura e imprime o erro
        else:
            print("Nenhum formulário válido foi enviado.")

    else:
        forms = [TabelaBrasileiraoForm(prefix=f'time_{i}', initial={'posicao': i}) for i in range(1, 21)]

    return render(request, 'cadastrar_tabela.html', {'forms': forms})



def mostrar_tabela(request):
    # Calcula os pontos e ordena pela quantidade de pontos
    tabela = list(
        TabelaBrasileirao.objects.annotate(
            pontos=F('vitorias') * 3 + F('empates')
        ).order_by('-pontos')
    )

    # Atualiza a posição dinamicamente
    for index, time in enumerate(tabela, start=1):
        time.posicao = index

    return render(request, 'mostrar_tabela.html', {'tabela': tabela})


# Create your views here.
def odd(request):
    return render(request, 'odd.html')
def login(request):
    return render(request,"login.html")
def Brasileirão(request):
    return render(request,"Brasileirão.html")
def budesliga(request):
    return render(request,"budesliga.html")
def BrasB(request):
    return render(request,"BrasB.html")
def espanhol(request):
    return render(request,"espanhol.html")
def ingles(request):
    return render(request,"ingles.html")
def italiano(request):
    return render(request,"italiano.html")
def frances(request):
    return render(request,"frances.html")