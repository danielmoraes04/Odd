from django.urls import path
from .views import odd, login, Brasileirão

urlpatterns = [
    path('', odd, name='odd'),
    path('login',login, name='login'),
    path('Brasileirão',Brasileirão, name='Brasileirão'),
]