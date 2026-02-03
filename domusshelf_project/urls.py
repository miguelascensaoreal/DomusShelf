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
from django.views.generic import RedirectView

urlpatterns = [
    # Painel de administração do Django
    path('admin/', admin.site.urls),
    
    # URLs de autenticação (login, logout, etc.)
    # O Django já fornece estas views, só precisamos dos templates
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Página inicial - por agora redireciona para o admin
    # Mais tarde vai apontar para o dashboard
    path('', RedirectView.as_view(url='/admin/', permanent=False)),
]