"""
DomusShelf - Views da Aplicação
===============================
Este ficheiro contém as views (controladores) que processam os pedidos
e devolvem as respostas ao utilizador.

Autor: Miguel Ângelo Ascensão Real
Data: 3 de Fevereiro de 2026
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    """
    Página inicial da aplicação (Dashboard).
    
    O decorador @login_required garante que apenas utilizadores
    autenticados podem aceder a esta página. Se não estiver autenticado,
    o Django redireciona automaticamente para LOGIN_URL.
    """
    context = {
        'titulo': 'Dashboard',
    }
    return render(request, 'pharmacy/dashboard.html', context)
