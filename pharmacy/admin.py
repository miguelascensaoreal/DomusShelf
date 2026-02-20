"""
DomusShelf - Configuração do Django Admin
==========================================
Este ficheiro configura como os modelos aparecem no painel de administração.
O Django Admin é uma interface automática que permite gerir os dados
sem precisar de criar páginas específicas.

Autor: Miguel Ângelo Ascensão Real
Data: 3 de Fevereiro de 2026
"""

from django.contrib import admin
from .models import Medicamento, Embalagem, Consumo, Preferencias


@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    """
    Configuração da página de administração de Medicamentos.
    """
    
    # Colunas que aparecem na listagem
    list_display = [
        'nome_comercial',
        'principio_activo',
        'forma_farmaceutica',
        'utilizador',
        'criado_em'
    ]
    
    # Campos pelos quais se pode pesquisar
    search_fields = [
        'nome_comercial',
        'principio_activo'
    ]
    
    # Filtros disponíveis na barra lateral
    list_filter = [
        'forma_farmaceutica',
        'utilizador'
    ]
    
    # Ordenação padrão
    ordering = ['nome_comercial']


@admin.register(Embalagem)
class EmbalagemAdmin(admin.ModelAdmin):
    """
    Configuração da página de administração de Embalagens.
    """
    
    list_display = [
        'medicamento',
        'quantidade_actual',
        'quantidade_inicial',
        'unidade',
        'data_validade',
        'lote',
        'estado_validade'
    ]
    
    search_fields = [
        'medicamento__nome_comercial',
        'lote'
    ]
    
    list_filter = [
        'data_validade',
        'medicamento__utilizador'
    ]
    
    # Ordenar por validade (FEFO)
    ordering = ['data_validade']
    
    # Método personalizado para mostrar o estado da validade
    @admin.display(description='Estado')
    def estado_validade(self, obj):
        """
        Mostra se a embalagem está expirada, a expirar, ou OK.
        """
        if obj.esta_expirada:
            return '❌ Expirado'
        elif obj.dias_para_expirar <= 30:
            return f'⚠️ Expira em {obj.dias_para_expirar} dias'
        else:
            return '✅ OK'


@admin.register(Consumo)
class ConsumoAdmin(admin.ModelAdmin):
    """
    Configuração da página de administração de Consumos.
    """
    
    list_display = [
        'embalagem',
        'quantidade',
        'data_hora',
        'observacoes'
    ]
    
    search_fields = [
        'embalagem__medicamento__nome_comercial',
        'observacoes'
    ]
    
    list_filter = [
        'data_hora',
        'embalagem__medicamento__utilizador'
    ]
    
    # Ordenar por data, mais recentes primeiro
    ordering = ['-data_hora']


@admin.register(Preferencias)
class PreferenciasAdmin(admin.ModelAdmin):
    """
    Configuração da página de administração de Preferências.
    """
    
    list_display = [
        'utilizador',
        'dias_alerta_antes'
    ]
    
    search_fields = [
        'utilizador__username'
    ]

from .models import Medicamento, Embalagem, Consumo, Preferencias, Familia, Convite

# (mantém os registos existentes, e adiciona:)

@admin.register(Familia)
class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'super_user', 'criado_em')

@admin.register(Convite)
class ConviteAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'familia', 'criado_por', 'criado_em', 'expira_em', 'usado_por', 'revogado')
    list_filter = ('revogado',)
    readonly_fields = ('codigo', 'criado_em')