from django.shortcuts import render, redirect
from django.http import JsonResponse

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