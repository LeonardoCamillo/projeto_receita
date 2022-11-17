from django.urls import path
from .views import cadastro, login, dashboard, logout, cria_receita


urlpatterns = [
    path('cadastro', cadastro, name='cadastro'),
    path('login', login, name='login'),
    path('dashboards', dashboard, name='dashboard'),
    path('logout', logout, name='logout'),
    path('criarReceita', cria_receita, name='cria_receita')
    ]