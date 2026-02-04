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
from . import views

# O app_name cria um "namespace" para evitar conflitos de nomes.
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
    path('<int:pk>/editar/', views.medicamento_editar, name='medicamento_editar'),
    
    # Página de confirmação para eliminar medicamento
    # URL completa será: /medicamentos/5/eliminar/
    path('<int:pk>/eliminar/', views.medicamento_eliminar, name='medicamento_eliminar'),
    
    # ==================== EMBALAGENS ====================
    # Lista de embalagens (stock) ordenada por validade
    # URL completa será: /embalagens/
    path('stock/', views.embalagem_lista, name='embalagem_lista'),
    
    # Formulário para adicionar nova embalagem ao stock
    # URL completa será: /embalagens/nova/
    path('stock/nova/', views.embalagem_criar, name='embalagem_criar'),
    
    # Formulário para editar embalagem existente
    # URL completa será: /embalagens/5/editar/
    path('stock/<int:pk>/editar/', views.embalagem_editar, name='embalagem_editar'),
    
    # Página de confirmação para eliminar embalagem
    # URL completa será: /embalagens/5/eliminar/
    path('stock/<int:pk>/eliminar/', views.embalagem_eliminar, name='embalagem_eliminar'),

    # Formulário para adicionar mbalagem existente
    path('consumo/novo/', views.consumo_criar, name='consumo_criar'),

    # Lista de alertas de embalagens expiradas ou a expirar
    path('alertas/', views.alertas_lista, name='alertas_lista'),
]