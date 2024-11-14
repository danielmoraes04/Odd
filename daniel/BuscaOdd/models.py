from django.db import models

class Jogo(models.Model):
    campeonato = models.CharField(max_length=255)
    time_casa = models.CharField(max_length=255)
    time_visitante = models.CharField(max_length=255)
    horario = models.TimeField()
    local_transmissao = models.CharField(max_length=255)
    link_transmissao = models.URLField(max_length=200)

