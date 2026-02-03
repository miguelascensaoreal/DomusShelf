"""
DomusShelf - Configuração de URLs Principal
============================================
Este ficheiro define as URLs principais da aplicação.
É o "mapa" que diz ao Django qual view deve responder a cada URL.

Autor: Miguel Ângelo Ascensão Real
Data: 3 de Fevereiro de 2026
"""

from django.contrib import admin
from django.urls import path, include

from pharmacy.views import dashboard

urlpatterns = [
    # Painel de administração do Django
    path('admin/', admin.site.urls),
    
    # URLs de autenticação (login, logout, etc.)
    path('accounts/', include('django.contrib.auth.urls')),
    
     # URLs da aplicação pharmacy (medicamentos)
    path('medicamentos/', include('pharmacy.urls')),

    # Página inicial - Dashboard
    path('', dashboard, name='dashboard'),
]