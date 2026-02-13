'''
DomusShelf - Views da Aplicação Pharmacy
========================================

Este ficheiro contém as views (controladores) que processam os pedidos HTTP
e devolvem as respostas apropriadas. Cada view é uma função que:
1. Recebe um objecto 'request' com informação sobre o pedido
2. Executa a lógica necessária (consultar BD, processar formulários, etc.)
3. Devolve um objecto 'response' (normalmente uma página HTML renderizada)

Autor: Miguel Ângelo Ascensão Real
Data: 3 de Fevereiro de 2026
'''

from datetime import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Medicamento, Embalagem, Consumo, Preferencias
from .forms import MedicamentoForm, EmbalagemForm, ConsumoForm, PreferenciasForm


# ==============================================================================
# DASHBOARD
# ==============================================================================

@login_required
def dashboard(request):
    """
    Página inicial da aplicação.
    Mostra estatísticas e uma visão geral do estado da farmácia.
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
    
    # Estatísticas
    total_medicamentos = Medicamento.objects.filter(
        utilizador=request.user
    ).count()
    
    embalagens_user = Embalagem.objects.filter(
        medicamento__utilizador=request.user,
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
    
    context = {
        'total_medicamentos': total_medicamentos,
        'total_embalagens': total_embalagens,
        'expiradas': expiradas,
        'a_expirar': a_expirar,
        'dias_alerta': dias_alerta,
    }
    return render(request, 'pharmacy/dashboard.html', context)


# ==============================================================================
# CRUD DE MEDICAMENTOS
# ==============================================================================

@login_required
def medicamento_lista(request):
    """
    Lista todos os medicamentos do utilizador autenticado.
    
    Importante: Filtramos por utilizador para que cada pessoa veja apenas
    os seus próprios medicamentos, não os de outros utilizadores.
    """
    # O request.user contém o utilizador autenticado (graças ao @login_required)
    # O .order_by ordena alfabeticamente pelo nome comercial
    medicamentos = Medicamento.objects.filter(
        utilizador=request.user
    ).order_by('nome_comercial')
    
    # Passamos a lista de medicamentos para o template através do 'context'
    context = {
        'medicamentos': medicamentos,
    }
    return render(request, 'pharmacy/medicamento_lista.html', context)


@login_required
def medicamento_criar(request):
    """
    Cria um novo medicamento.
    
    Esta view trata dois tipos de pedido:
    - GET: O utilizador acabou de aceder à página → mostramos formulário vazio
    - POST: O utilizador submeteu o formulário → validamos e guardamos
    """
    if request.method == 'POST':
        # O utilizador submeteu o formulário
        # Criamos o form com os dados recebidos (request.POST)
        form = MedicamentoForm(request.POST)
        
        if form.is_valid():
            # Os dados são válidos! Vamos guardar.
            # O commit=False cria o objecto mas NÃO guarda na BD ainda.
            # Isto permite-nos adicionar o utilizador antes de guardar.
            medicamento = form.save(commit=False)
            medicamento.utilizador = request.user  # Associar ao utilizador actual
            medicamento.save()  # Agora sim, guardar na base de dados
            
            # Redirecionar para a lista (evita resubmissão se o utilizador
            # carregar F5/actualizar a página)
            return redirect('pharmacy:medicamento_lista')
    else:
        # Pedido GET: mostrar formulário vazio
        form = MedicamentoForm()
    
    context = {
        'form': form,
        'titulo': 'Novo Medicamento',  # Usado no template para o título da página
    }
    return render(request, 'pharmacy/medicamento_form.html', context)


@login_required
def medicamento_editar(request, pk):
    """
    Edita um medicamento existente.
    
    Parâmetros:
        pk: Primary Key (ID) do medicamento a editar, vem da URL
    
    Segurança: Verificamos que o medicamento pertence ao utilizador actual.
    O get_object_or_404 devolve erro 404 se não encontrar o medicamento.
    """
    # Buscar o medicamento OU devolver página 404 se não existir
    # Filtramos também por utilizador para segurança (um utilizador não pode
    # editar medicamentos de outro)
    medicamento = get_object_or_404(
        Medicamento,
        pk=pk,
        utilizador=request.user
    )
    
    if request.method == 'POST':
        # instance=medicamento diz ao form para actualizar este objecto
        # em vez de criar um novo
        form = MedicamentoForm(request.POST, instance=medicamento)
        
        if form.is_valid():
            form.save()  # Não precisamos de commit=False porque o utilizador já está definido
            return redirect('pharmacy:medicamento_lista')
    else:
        # Pedido GET: mostrar formulário preenchido com dados actuais
        form = MedicamentoForm(instance=medicamento)
    
    context = {
        'form': form,
        'titulo': 'Editar Medicamento',
        'medicamento': medicamento,  # Útil para mostrar info extra no template
    }
    return render(request, 'pharmacy/medicamento_form.html', context)


@login_required
def medicamento_eliminar(request, pk):
    """
    Elimina um medicamento após confirmação.
    
    Por segurança, a eliminação requer um pedido POST (não basta aceder ao URL).
    Primeiro mostramos uma página de confirmação (GET), e só eliminamos
    quando o utilizador confirma (POST).
    """
    medicamento = get_object_or_404(
        Medicamento,
        pk=pk,
        utilizador=request.user
    )
    
    if request.method == 'POST':
        # O utilizador confirmou a eliminação
        medicamento.delete()
        return redirect('pharmacy:medicamento_lista')
    
    # Pedido GET: mostrar página de confirmação
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
    Lista todas as embalagens do utilizador, ordenadas por data de validade.
    
    A ordenação segue o princípio FEFO (First Expired, First Out):
    embalagens que expiram mais cedo aparecem primeiro, incentivando
    o utilizador a consumir primeiro o que está prestes a expirar.
    
    Filtramos por medicamento__utilizador porque a Embalagem não tem
    relação directa com User — a relação é através do Medicamento.
    """
    from datetime import date
    
    # Buscar embalagens cujo medicamento pertence ao utilizador actual
    # O duplo underscore (medicamento__utilizador) atravessa a relação ForeignKey
    embalagens = Embalagem.objects.filter(
        medicamento__utilizador=request.user
    ).select_related('medicamento').order_by('data_validade')
    
    # select_related('medicamento') é uma optimização: carrega os dados do
    # medicamento na mesma query, evitando queries adicionais quando acedemos
    # a embalagem.medicamento no template (problema N+1)
    
    context = {
        'embalagens': embalagens,
        'hoje': date.today(),  # Passamos a data de hoje para comparações no template
    }
    return render(request, 'pharmacy/embalagem_lista.html', context)


@login_required
def embalagem_criar(request):
    """
    Cria uma nova embalagem (adiciona stock).
    
    O formulário inclui um dropdown para seleccionar o medicamento.
    Esse dropdown é filtrado para mostrar apenas medicamentos do utilizador.
    """
    if request.method == 'POST':
        form = EmbalagemForm(request.POST, user=request.user)
        
        if form.is_valid():
            embalagem = form.save(commit=False)
            # Definir quantidade_actual igual à quantidade_inicial
            # (embalagem nova, ainda não foi consumida)
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
    
    Segurança: Verificamos que a embalagem pertence a um medicamento
    do utilizador actual (através da relação medicamento__utilizador).
    """
    embalagem = get_object_or_404(
        Embalagem,
        pk=pk,
        medicamento__utilizador=request.user
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
    
    A eliminação de uma embalagem também elimina todos os consumos
    associados (definido pelo on_delete=CASCADE no modelo).
    """
    embalagem = get_object_or_404(
        Embalagem,
        pk=pk,
        medicamento__utilizador=request.user
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
    View para registar um novo consumo/toma.
    Ao guardar, desconta automaticamente a quantidade da embalagem.
    """
    if request.method == 'POST':
        form = ConsumoForm(request.POST, user=request.user)
        if form.is_valid():
            consumo = form.save(commit=False)
            consumo.data_hora = timezone.now()  # Define a data/hora actual

            # Desconta a quantidade da embalagem
            embalagem = consumo.embalagem
            embalagem.quantidade_actual -= consumo.quantidade
            embalagem.save()
            
            # Agora guarda o consumo
            consumo.save()
            
            return redirect('pharmacy:embalagem_lista')
    else:
        form = ConsumoForm(user=request.user)
    
    return render(request, 'pharmacy/consumo_form.html', {'form': form})

@login_required
def alertas_lista(request):
    """
    Página que lista todas as embalagens expiradas ou a expirar em breve.
    Separadas em duas secções: expiradas e a expirar.
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
    
    # Embalagens do utilizador com stock
    embalagens_user = Embalagem.objects.filter(
        medicamento__utilizador=request.user,
        quantidade_actual__gt=0
    ).select_related('medicamento')
    
    # Separar em expiradas e a expirar
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
    View para editar as preferências do utilizador.
    
    CONCEITO NOVO: get_or_create()
    Este método tenta obter um objecto da base de dados.
    Se não existir, cria-o automaticamente.
    
    Retorna uma tupla: (objecto, foi_criado)
    - objecto: a instância do modelo
    - foi_criado: True se criou novo, False se já existia
    
    Isto é útil aqui porque um utilizador novo pode não ter
    preferências ainda criadas.
    """
    # Obter ou criar as preferências do utilizador
    preferencias, criado = Preferencias.objects.get_or_create(
        utilizador=request.user,
        defaults={'dias_alerta_antes': 30}  # Valores por defeito se criar novo
    )
    
    if request.method == 'POST':
        form = PreferenciasForm(request.POST, instance=preferencias)
        if form.is_valid():
            form.save()
            # Redirecionar para o dashboard após guardar
            return redirect('dashboard')
    else:
        # GET: mostrar formulário preenchido com valores actuais
        form = PreferenciasForm(instance=preferencias)
    
    return render(request, 'pharmacy/preferencias_form.html', {
        'form': form,
    })

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def registo(request):
    """
    View para registo de novos utilizadores.
    Não usa @login_required porque o utilizador ainda não tem conta.
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