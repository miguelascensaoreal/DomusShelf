# pharmacy/urls.py
# ================
# Este ficheiro define as URLs específicas da aplicação pharmacy.
# Cada URL mapeia um caminho (path) para uma view que processa o pedido.
#
# Estrutura: path('caminho/', view, name='nome_único')
# - 'caminho/' é o que aparece no browser (relativo ao prefixo da app)
# - view é a função ou classe que processa o pedido
# - name é um identificador único usado nos templates para gerar URLs

from django.urls import path
from . import views  # Importa as views do ficheiro views.py desta app

# O app_name cria um "namespace" para evitar conflitos de nomes.
# Nos templates, usaremos {% url 'pharmacy:medicamento_lista' %} em vez de
# apenas {% url 'medicamento_lista' %}. Isto é útil quando temos várias apps.
app_name = 'pharmacy'

urlpatterns = [
    # ==================== MEDICAMENTOS ====================
    # Lista de medicamentos do utilizador
    # URL completa será: /medicamentos/
    path('', views.medicamento_lista, name='medicamento_lista'),
    
    # Formulário para criar novo medicamento
    # URL completa será: /medicamentos/novo/
    path('novo/', views.medicamento_criar, name='medicamento_criar'),
    
    # Formulário para editar medicamento existente
    # URL completa será: /medicamentos/5/editar/ (onde 5 é o ID)
    # <int:pk> captura um número inteiro e passa-o à view como argumento 'pk'
    path('<int:pk>/editar/', views.medicamento_editar, name='medicamento_editar'),
    
    # Página de confirmação para eliminar medicamento
    # URL completa será: /medicamentos/5/eliminar/
    path('<int:pk>/eliminar/', views.medicamento_eliminar, name='medicamento_eliminar'),
]