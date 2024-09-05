from django.urls import path
from .views import odd, login

urlpatterns = [
    path('', odd, name='odd'),
    path('login',login, name='login'),
]