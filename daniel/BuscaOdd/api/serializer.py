from rest_framework import serializers
from BuscaOdd import models

class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Jogo
        fields = '__all__'

class TabelaBrasileiraoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TabelaBrasileirao
        fields = '__all__'