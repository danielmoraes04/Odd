from django.urls import path
from .api.viewsets import JogoViewSets, TabelaBrasileiraoViewSets
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


    # URLS COM USO DE BANCO DE DADOS:

    path('jogos', views.jogos_view, name='jogos'),
    path('visualizar', views.visualizar_jogos, name='Visualizar'),
    path('cadastrar_tabela/', views.cadastrar_tabela, name='cadastrar_tabela'),
    path('mostrar/', views.mostrar_tabela, name='mostrar_tabela'),
    path('deletar-jogo/<int:id>/', views.deletar_jogo, name='deletar_jogo'),
    path('api/tabela', TabelaBrasileiraoViewSets.as_view(), name='tabela-list'),
    path('api/tabela/<str:id>',TabelaBrasileiraoViewSets.as_view(),name='tabela-detalhe'),
    path('api/jogo', JogoViewSets.as_view(), name='jogo-list'),
    path('api/jogo/<str:id>',JogoViewSets.as_view(),name='jogo-detalhe')
]