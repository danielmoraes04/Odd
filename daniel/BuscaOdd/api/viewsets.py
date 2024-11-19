from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from BuscaOdd.api import serializer
from BuscaOdd.models import Jogo, TabelaBrasileirao
from BuscaOdd.api.serializer import JogoSerializer, TabelaBrasileiraoSerializer

class JogoViewSets(APIView):
    def get(self, request, id=None):
        if id:
            jogo = get_object_or_404(Jogo, id=id)
            serializer = JogoSerializer(jogo)
            return Response(serializer.data)
        items = Jogo.objects.all()
        serializer = JogoSerializer(items, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = JogoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        item = get_object_or_404(Jogo,id=id)
        serializer = JogoSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        item = get_object_or_404(Jogo, id=id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TabelaBrasileiraoViewSets(APIView):

    def get(self, request, id=None):
        if id:
            tabela = get_object_or_404(TabelaBrasileirao, id=id)
            serializer = TabelaBrasileiraoSerializer(tabela)
            return Response(serializer.data)
        items = TabelaBrasileirao.objects.all()
        serializer = TabelaBrasileiraoSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TabelaBrasileiraoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)