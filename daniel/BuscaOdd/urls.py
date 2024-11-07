from django.urls import path
from . import views
from .views import odd, login, Brasileirão, budesliga, BrasB, espanhol, frances, ingles, italiano

urlpatterns = [
    path('agenda', odd, name='odd'),
    path('login',login, name='login'),
    path('brasileirão',Brasileirão, name='Brasileirão'),
    path('bundesliga',budesliga, name='budesliga'),
    path('brasileirãosérieb',BrasB, name='BrasB'),
    path('laliga',espanhol, name='espanhol'),
    path('ligue1',frances, name='frances'),
    path('premierleague',ingles, name='ingles'),
    path('seriea', italiano, name='italiano'),
    path('jogos', views.jogos_view, name='jogos'),
    path('visualizar', views.visualizar_jogos, name='Visualizar')
]