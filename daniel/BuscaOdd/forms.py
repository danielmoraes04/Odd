from django import forms
from .models import Jogo


class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = ['campeonato', 'time_casa', 'time_visitante', 'horario', 'local_transmissao', 'link_transmissao']