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

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Medicamento, Embalagem
from .forms import MedicamentoForm, EmbalagemForm


# ==============================================================================
# DASHBOARD
# ==============================================================================

@login_required
def dashboard(request):
    """
    Página inicial da aplicação.
    Mostra uma visão geral com cards de acesso rápido às funcionalidades.
    """
    return render(request, 'pharmacy/dashboard.html')


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