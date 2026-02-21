"""
DomusShelf - Funções Auxiliares
===============================
Funções utilitárias partilhadas pelas views.
"""

import logging

logger = logging.getLogger(__name__)

def get_medicamentos_for_user(user):
    """
    Devolve os medicamentos visíveis para o utilizador.
    
    Se o utilizador pertence a uma família, devolve os medicamentos da família.
    Se não pertence, devolve apenas os seus (modo individual v1).
    
    Isto centraliza a lógica de filtragem para manter o código DRY.
    """
    from pharmacy.models import Medicamento
    
    try:
        familia = user.preferencias.familia
    except Exception:
        familia = None
    
    if familia:
        return Medicamento.objects.filter(familia=familia)
    else:
        return Medicamento.objects.filter(utilizador=user, familia__isnull=True)


def get_familia_for_user(user):
    """
    Devolve a família do utilizador, ou None se não pertencer a nenhuma.
    """
    try:
        return user.preferencias.familia
    except Exception:
        return None


def is_super_user(user):
    """
    Verifica se o utilizador é o Super User da sua família.
    """
    familia = get_familia_for_user(user)
    if familia:
        return familia.super_user == user
    return False

def registar_actividade(user, tipo, descricao):
    """
    Regista uma acção no logbook da família do utilizador.
    Se o utilizador não pertence a uma família, não faz nada (silenciosamente).
    
    Parâmetros:
        user: o utilizador que realizou a acção
        tipo: string com o tipo (ex: 'medicamento_criado')
        descricao: texto livre descrevendo o que aconteceu
    """
    from pharmacy.models import RegistoActividade
    
    familia = get_familia_for_user(user)
    if not familia:
        return  # Sem família, sem logbook
    
    try:
        RegistoActividade.objects.create(
            familia=familia,
            utilizador=user,
            tipo=tipo,
            descricao=descricao
        )
    except Exception as e:
        # O logbook nunca deve impedir uma acção de funcionar
        logger.error(f"Erro ao registar actividade: {e}")