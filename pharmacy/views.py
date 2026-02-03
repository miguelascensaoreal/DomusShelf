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

from .models import Medicamento
from .forms import MedicamentoForm  # Vamos criar este ficheiro a seguir


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
