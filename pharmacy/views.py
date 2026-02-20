'''
DomusShelf - Views da Aplicação Pharmacy
========================================
Autor: Miguel Ângelo Ascensão Real
Data: 3 de Fevereiro de 2026
Actualizado: Fevereiro de 2026 (v2 — Conceito de Família)
'''

from datetime import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Medicamento, Embalagem, Consumo, Preferencias
from .forms import MedicamentoForm, EmbalagemForm, ConsumoForm, PreferenciasForm
from .utils import get_medicamentos_for_user, get_familia_for_user


# ==============================================================================
# DASHBOARD
# ==============================================================================

@login_required
def dashboard(request):
    """
    Página inicial da aplicação.
    v2: Mostra dados da família se o utilizador pertencer a uma.
    """
    from datetime import date, timedelta
    hoje = date.today()

    # Obter preferências do utilizador
    try:
        prefs = Preferencias.objects.get(utilizador=request.user)
        dias_alerta = prefs.dias_alerta_antes
    except Preferencias.DoesNotExist:
        dias_alerta = 30

    data_limite = hoje + timedelta(days=dias_alerta)

    # v2: Usar função auxiliar para obter medicamentos (família ou individual)
    medicamentos = get_medicamentos_for_user(request.user)

    # Estatísticas
    total_medicamentos = medicamentos.count()

    # v2: Embalagens filtradas pelos medicamentos visíveis (família ou individual)
    embalagens_user = Embalagem.objects.filter(
        medicamento__in=medicamentos,
        quantidade_actual__gt=0
    )

    total_embalagens = embalagens_user.count()

    expiradas = embalagens_user.filter(
        data_validade__lt=hoje
    ).count()

    a_expirar = embalagens_user.filter(
        data_validade__gte=hoje,
        data_validade__lte=data_limite
    ).count()

    # v2: Informação da família para o template
    familia = get_familia_for_user(request.user)

    context = {
        'total_medicamentos': total_medicamentos,
        'total_embalagens': total_embalagens,
        'expiradas': expiradas,
        'a_expirar': a_expirar,
        'dias_alerta': dias_alerta,
        'familia': familia,
    }

    return render(request, 'pharmacy/dashboard.html', context)


# ==============================================================================
# CRUD DE MEDICAMENTOS
# ==============================================================================

@login_required
def medicamento_lista(request):
    """
    Lista medicamentos.
    v2: Mostra medicamentos da família se o utilizador pertencer a uma.
    """
    medicamentos = get_medicamentos_for_user(request.user).order_by('nome_comercial')

    context = {
        'medicamentos': medicamentos,
    }
    return render(request, 'pharmacy/medicamento_lista.html', context)


@login_required
def medicamento_criar(request):
    """
    Cria um novo medicamento.
    v2: Associa à família do utilizador, se existir.
    """
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            medicamento = form.save(commit=False)
            medicamento.utilizador = request.user

            # v2: Associar à família do utilizador
            familia = get_familia_for_user(request.user)
            if familia:
                medicamento.familia = familia

            medicamento.save()
            return redirect('pharmacy:medicamento_lista')
    else:
        form = MedicamentoForm()

    context = {
        'form': form,
        'titulo': 'Novo Medicamento',
    }
    return render(request, 'pharmacy/medicamento_form.html', context)


@login_required
def medicamento_editar(request, pk):
    """
    Edita um medicamento existente.
    v2: Permite editar medicamentos da família.
    """
    # v2: Buscar entre os medicamentos visíveis ao utilizador
    medicamentos_visiveis = get_medicamentos_for_user(request.user)
    medicamento = get_object_or_404(medicamentos_visiveis, pk=pk)

    if request.method == 'POST':
        form = MedicamentoForm(request.POST, instance=medicamento)
        if form.is_valid():
            form.save()
            return redirect('pharmacy:medicamento_lista')
    else:
        form = MedicamentoForm(instance=medicamento)

    context = {
        'form': form,
        'titulo': 'Editar Medicamento',
        'medicamento': medicamento,
    }
    return render(request, 'pharmacy/medicamento_form.html', context)


@login_required
def medicamento_eliminar(request, pk):
    """
    Elimina um medicamento após confirmação.
    v2: Permite eliminar medicamentos da família.
    """
    medicamentos_visiveis = get_medicamentos_for_user(request.user)
    medicamento = get_object_or_404(medicamentos_visiveis, pk=pk)

    if request.method == 'POST':
        medicamento.delete()
        return redirect('pharmacy:medicamento_lista')

    context = {
        'medicamento': medicamento,
    }
    return render(request, 'pharmacy/medicamento_confirmar_eliminar.html', context)


# ==============================================================================
# CRUD DE EMBALAGENS (STOCK)
# ==============================================================================

@login_required
def embalagem_lista(request):
    """
    Lista embalagens.
    v2: Mostra embalagens da família se o utilizador pertencer a uma.
    """
    from datetime import date

    # v2: Filtrar embalagens pelos medicamentos visíveis ao utilizador
    medicamentos = get_medicamentos_for_user(request.user)
    embalagens = Embalagem.objects.filter(
        medicamento__in=medicamentos
    ).select_related('medicamento').order_by('data_validade')

    context = {
        'embalagens': embalagens,
        'hoje': date.today(),
    }
    return render(request, 'pharmacy/embalagem_lista.html', context)


@login_required
def embalagem_criar(request):
    """
    Cria uma nova embalagem (adiciona stock).
    v2: Passa a família ao formulário para filtrar medicamentos.
    """
    if request.method == 'POST':
        form = EmbalagemForm(request.POST, user=request.user)
        if form.is_valid():
            embalagem = form.save(commit=False)
            embalagem.quantidade_actual = embalagem.quantidade_inicial
            embalagem.save()
            return redirect('pharmacy:embalagem_lista')
    else:
        form = EmbalagemForm(user=request.user)

    context = {
        'form': form,
        'titulo': 'Nova Embalagem',
    }
    return render(request, 'pharmacy/embalagem_form.html', context)


@login_required
def embalagem_editar(request, pk):
    """
    Edita uma embalagem existente.
    v2: Permite editar embalagens da família.
    """
    # v2: Buscar entre embalagens dos medicamentos visíveis
    medicamentos = get_medicamentos_for_user(request.user)
    embalagem = get_object_or_404(
        Embalagem,
        pk=pk,
        medicamento__in=medicamentos
    )

    if request.method == 'POST':
        form = EmbalagemForm(request.POST, instance=embalagem, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('pharmacy:embalagem_lista')
    else:
        form = EmbalagemForm(instance=embalagem, user=request.user)

    context = {
        'form': form,
        'titulo': 'Editar Embalagem',
        'embalagem': embalagem,
    }
    return render(request, 'pharmacy/embalagem_form.html', context)


@login_required
def embalagem_eliminar(request, pk):
    """
    Elimina uma embalagem após confirmação.
    v2: Permite eliminar embalagens da família.
    """
    medicamentos = get_medicamentos_for_user(request.user)
    embalagem = get_object_or_404(
        Embalagem,
        pk=pk,
        medicamento__in=medicamentos
    )

    if request.method == 'POST':
        embalagem.delete()
        return redirect('pharmacy:embalagem_lista')

    context = {
        'embalagem': embalagem,
    }
    return render(request, 'pharmacy/embalagem_confirmar_eliminar.html', context)


@login_required
def consumo_criar(request):
    """
    Regista um novo consumo/toma.
    v2: Associa o consumo ao utilizador e filtra embalagens da família.
    """
    if request.method == 'POST':
        form = ConsumoForm(request.POST, user=request.user)
        if form.is_valid():
            consumo = form.save(commit=False)
            consumo.data_hora = timezone.now()

            # v2: Associar o consumo ao utilizador
            consumo.utilizador = request.user

            # Desconta a quantidade da embalagem
            embalagem = consumo.embalagem
            embalagem.quantidade_actual -= consumo.quantidade
            embalagem.save()

            consumo.save()
            return redirect('pharmacy:embalagem_lista')
    else:
        form = ConsumoForm(user=request.user)

    return render(request, 'pharmacy/consumo_form.html', {'form': form})


@login_required
def alertas_lista(request):
    """
    Lista embalagens expiradas ou a expirar.
    v2: Mostra alertas da família.
    """
    from datetime import date, timedelta
    hoje = date.today()

    try:
        prefs = Preferencias.objects.get(utilizador=request.user)
        dias_alerta = prefs.dias_alerta_antes
    except Preferencias.DoesNotExist:
        dias_alerta = 30

    data_limite = hoje + timedelta(days=dias_alerta)

    # v2: Embalagens dos medicamentos visíveis ao utilizador
    medicamentos = get_medicamentos_for_user(request.user)
    embalagens_user = Embalagem.objects.filter(
        medicamento__in=medicamentos,
        quantidade_actual__gt=0
    ).select_related('medicamento')

    expiradas = embalagens_user.filter(
        data_validade__lt=hoje
    ).order_by('data_validade')

    a_expirar = embalagens_user.filter(
        data_validade__gte=hoje,
        data_validade__lte=data_limite
    ).order_by('data_validade')

    context = {
        'expiradas': expiradas,
        'a_expirar': a_expirar,
        'dias_alerta': dias_alerta,
        'hoje': hoje,
    }
    return render(request, 'pharmacy/alertas_lista.html', context)


@login_required
def preferencias_editar(request):
    """
    Edita as preferências do utilizador.
    """
    preferencias, criado = Preferencias.objects.get_or_create(
        utilizador=request.user,
        defaults={'dias_alerta_antes': 30}
    )

    if request.method == 'POST':
        form = PreferenciasForm(request.POST, instance=preferencias)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PreferenciasForm(instance=preferencias)

    return render(request, 'pharmacy/preferencias_form.html', {
        'form': form,
    })


from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def registo(request):
    """
    View para registo de novos utilizadores.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso! Já pode iniciar sessão.')
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/registo.html', {'form': form})