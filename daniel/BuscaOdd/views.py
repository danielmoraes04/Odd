from django.shortcuts import render, redirect
from .models import Jogo
from .forms import JogoForm
from django.http import JsonResponse
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