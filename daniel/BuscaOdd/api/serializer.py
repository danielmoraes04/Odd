from rest_framework import serializers
from BuscaOdd import models

class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Jogo
        fields = '__all__'