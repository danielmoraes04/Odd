from django import forms
from .models import Jogo
from .models import TabelaBrasileirao

class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = ['campeonato', 'time_casa', 'time_visitante', 'horario', 'local_transmissao', 'link_transmissao']

class TabelaBrasileiraoForm(forms.ModelForm):
    class Meta:
        model = TabelaBrasileirao
        fields = ['posicao', 'time', 'jogos', 'vitorias', 'empates', 'derrotas']
        widgets = {
            'posicao': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do time'}),
            'jogos': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total de jogos'}),
            'vitorias': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de vitórias'}),
            'empates': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de empates'}),
            'derrotas': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de derrotas'}),
        }