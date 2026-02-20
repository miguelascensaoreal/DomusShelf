'''
DomusShelf - Context Processors
===============================

Context processors são funções que adicionam variáveis ao contexto
de TODOS os templates automaticamente. Útil para dados que aparecem
em todas as páginas, como a contagem de alertas no sino.

Autor: Miguel Ângelo Ascensão Real
Data: 4 de Fevereiro de 2026
'''

from datetime import date, timedelta
from urllib import request
from .models import Embalagem, Preferencias


def alertas_count(request):
    """
    Adiciona a contagem de alertas ao contexto de todos os templates.
    
    Calcula:
    - Embalagens já expiradas
    - Embalagens a expirar dentro dos próximos X dias (configurável)
    
    Retorna um dicionário que é adicionado ao contexto de cada template.
    """
    if not request.user.is_authenticated:
        return {'alertas_count': 0}
    
    hoje = date.today()
    
    # Obter preferências do utilizador (dias de antecedência para alertas)
    try:
        prefs = Preferencias.objects.get(utilizador=request.user)
        dias_alerta = prefs.dias_alerta_antes
    except Preferencias.DoesNotExist:
        dias_alerta = 30  # Valor por defeito
    
    data_limite = hoje + timedelta(days=dias_alerta)
    
    # Contar embalagens problemáticas (expiradas OU a expirar em breve)
    # Filtramos apenas embalagens com stock > 0 (não faz sentido alertar sobre vazias)
    from .utils import get_medicamentos_for_user
    medicamentos = get_medicamentos_for_user(request.user)
    
    count = Embalagem.objects.filter(
        medicamento__in=medicamentos,
        quantidade_actual__gt=0,
        data_validade__lte=data_limite
    ).count()
    
    return {'alertas_count': count}