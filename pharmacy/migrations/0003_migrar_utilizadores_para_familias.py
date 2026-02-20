"""
Data migration: Cria uma Família para cada utilizador existente
e associa os seus medicamentos e preferências a essa família.
"""

from django.db import migrations


def criar_familias_para_utilizadores(apps, schema_editor):
    """
    Para cada utilizador que já tenha medicamentos, cria uma Família
    e associa tudo a ela. Isto garante que os dados da v1 ficam
    correctamente ligados ao novo modelo de família.
    """
    User = apps.get_model('auth', 'User')
    Familia = apps.get_model('pharmacy', 'Familia')
    Medicamento = apps.get_model('pharmacy', 'Medicamento')
    Preferencias = apps.get_model('pharmacy', 'Preferencias')
    Consumo = apps.get_model('pharmacy', 'Consumo')
    
    for user in User.objects.all():
        # Verificar se o utilizador tem medicamentos
        medicamentos = Medicamento.objects.filter(utilizador=user)
        if not medicamentos.exists():
            continue
        
        # Criar a família
        familia = Familia.objects.create(
            nome=f"Família de {user.username}",
            super_user=user
        )
        
        # Associar medicamentos à família
        medicamentos.update(familia=familia)
        
        # Associar preferências à família
        try:
            prefs = Preferencias.objects.get(utilizador=user)
            prefs.familia = familia
            prefs.save()
        except Preferencias.DoesNotExist:
            pass
        
        # Associar consumos ao utilizador
        # Na v1 o consumo não tinha campo utilizador directo
        # Vamos preencher com base no dono do medicamento da embalagem
        for med in medicamentos:
            for embalagem in med.embalagens.all():
                Consumo.objects.filter(
                    embalagem=embalagem,
                    utilizador__isnull=True
                ).update(utilizador=user)


def reverter_familias(apps, schema_editor):
    """Reversão: remove todas as famílias criadas automaticamente."""
    Familia = apps.get_model('pharmacy', 'Familia')
    Medicamento = apps.get_model('pharmacy', 'Medicamento')
    Preferencias = apps.get_model('pharmacy', 'Preferencias')
    
    Medicamento.objects.all().update(familia=None)
    Preferencias.objects.all().update(familia=None)
    Familia.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0002_consumo_anulado_consumo_anulado_em_and_more'),
    ]

    operations = [
        migrations.RunPython(
            criar_familias_para_utilizadores,
            reverter_familias
        ),
    ]