from django.shortcuts import render

# Create your views here.
def odd(request):
    return render(request, 'odd.html')
def login(request):
    return render(request,"login.html")
def Brasileirão(request):
    return render(request,"Brasileirão.html")