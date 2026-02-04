'''
DomusShelf - Formulários da Aplicação Pharmacy
==============================================

Este ficheiro define os formulários (forms) usados na aplicação.
Usamos ModelForms que geram formulários automaticamente a partir dos modelos,
evitando duplicação de código e mantendo consistência.

Autor: Miguel Ângelo Ascensão Real
Data: 3 de Fevereiro de 2026
'''

from django import forms
from .models import Medicamento, Embalagem, Consumo, Preferencias


class MedicamentoForm(forms.ModelForm):
    """
    Formulário para criar e editar medicamentos.
    
    Herda de ModelForm, o que significa que os campos são gerados
    automaticamente a partir do modelo Medicamento.
    """
    
    class Meta:
        """
        A classe Meta configura o comportamento do ModelForm.
        É aqui que dizemos qual modelo usar e quais campos incluir.
        """
        # Qual modelo este form representa
        model = Medicamento
        
        # Quais campos incluir no formulário
        # NOTA: Não incluímos 'utilizador' nem 'criado_em' porque:
        # - utilizador: é definido automaticamente na view (request.user)
        # - criado_em: é preenchido automaticamente pelo Django (auto_now_add)
        fields = ['nome_comercial', 'principio_activo', 'forma_farmaceutica', 'observacoes']
        
        # Labels personalizados (o que aparece antes de cada campo)
        # Se não definirmos, o Django usa o nome do campo com primeira letra maiúscula
        labels = {
            'nome_comercial': 'Nome Comercial',
            'principio_activo': 'Princípio Activo',
            'forma_farmaceutica': 'Forma Farmacêutica',
            'observacoes': 'Observações',
        }
        
        # Widgets personalizados (controlam como o campo é renderizado em HTML)
        # Aqui adicionamos classes CSS do Bootstrap para estilização
        widgets = {
            'nome_comercial': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Ben-u-ron',
            }),
            'principio_activo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Paracetamol',
            }),
            'forma_farmaceutica': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Comprimidos, Xarope, Pomada',
            }),
            'observacoes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Notas adicionais (opcional)',
            }),
        }
        
        # Textos de ajuda (aparecem abaixo do campo)
        help_texts = {
            'principio_activo': 'Substância activa do medicamento',
            'forma_farmaceutica': 'Como o medicamento se apresenta',
        }
        
class EmbalagemForm(forms.ModelForm):
    """
    Formulário para criar e editar embalagens (stock).
    
    Este formulário é mais complexo que o MedicamentoForm porque:
    1. O campo 'medicamento' precisa de ser filtrado por utilizador
    2. O campo 'data_validade' precisa de um widget de data
    3. Não incluímos 'quantidade_actual' (é calculado automaticamente)
    """
    
    class Meta:
        model = Embalagem
        
        # Campos a incluir no formulário
        # NOTA: Não incluímos 'quantidade_actual' porque:
        # - Na criação: é igual a quantidade_inicial (definido na view)
        # - Na edição: só muda através de consumos, não manualmente
        # NOTA: Não incluímos 'criado_em' (preenchido automaticamente)
        fields = ['medicamento', 'quantidade_inicial', 'unidade', 'data_validade', 'lote']
        
        labels = {
            'medicamento': 'Medicamento',
            'quantidade_inicial': 'Quantidade',
            'unidade': 'Unidade',
            'data_validade': 'Data de Validade',
            'lote': 'Lote',
        }
        
        widgets = {
            'medicamento': forms.Select(attrs={
                'class': 'form-select',  # form-select é a classe Bootstrap para dropdowns
            }),
            'quantidade_inicial': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',  # Não faz sentido ter quantidade 0 ou negativa
                'placeholder': 'Ex: 20',
            }),
            'unidade': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: comprimidos, ml, doses',
            }),
            'data_validade': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'class': 'form-control',
                    'placeholder': 'dd/mm/aaaa',
                }
            ),
            'lote': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: ABC123 (opcional)',
            }),
        }
        
        help_texts = {
            'quantidade_inicial': 'Número de unidades na embalagem',
            'lote': 'Número do lote (encontra-se na embalagem)',
            'data_validade': 'Formato: dd/mm/aaaa (exemplo: 05/02/2026)',
        }
    
    def __init__(self, *args, **kwargs):
        """
        Construtor personalizado para receber o utilizador.
        
        Este método é chamado quando criamos uma instância do formulário.
        Usamo-lo para filtrar o queryset do campo 'medicamento', mostrando
        apenas os medicamentos que pertencem ao utilizador actual.
        
        O padrão é:
        1. Extrair o 'user' dos kwargs (argumentos nomeados)
        2. Chamar o __init__ da classe pai (super)
        3. Modificar o queryset do campo que queremos filtrar
        """
        # Extrair o utilizador dos kwargs ANTES de chamar super()
        # O pop() remove o 'user' do dicionário, evitando erro no super()
        # (porque o ModelForm não espera um argumento 'user')
        user = kwargs.pop('user', None)
        
        # Chamar o construtor da classe pai
        super().__init__(*args, **kwargs)
        
        # Filtrar o dropdown de medicamentos para mostrar apenas os do utilizador
        if user:
            self.fields['medicamento'].queryset = Medicamento.objects.filter(
                utilizador=user
            ).order_by('nome_comercial')

class ConsumoForm(forms.ModelForm):
    """
    Formulário para registar consumos/tomas de medicamentos.
    Filtra as embalagens para mostrar apenas as do utilizador actual
    e valida que não se consome mais do que a quantidade disponível.
    """
    
    class Meta:
        model = Consumo
        fields = ['embalagem', 'quantidade', 'observacoes']
        widgets = {
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        # Extrai o user antes de chamar o __init__ pai
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # Filtra embalagens: apenas as do utilizador E com stock > 0
        if self.user:
            self.fields['embalagem'].queryset = Embalagem.objects.filter(
                medicamento__utilizador=self.user,
                quantidade_actual__gt=0  # Só mostra embalagens com stock
            ).select_related('medicamento').order_by('data_validade')
        # Adiciona classes Bootstrap aos campos
        self.fields['embalagem'].widget.attrs.update({'class': 'form-select'})
        self.fields['quantidade'].widget.attrs.update({'class': 'form-control'})
        self.fields['observacoes'].widget.attrs.update({'class': 'form-control'})
    
    def clean(self):
        """
        Validação personalizada: garante que a quantidade a consumir
        não excede a quantidade disponível na embalagem.
        """
        cleaned_data = super().clean()
        embalagem = cleaned_data.get('embalagem')
        quantidade = cleaned_data.get('quantidade')
        
        if embalagem and quantidade:
            if quantidade > embalagem.quantidade_actual:
                raise forms.ValidationError(
                    f'Quantidade indisponível. Esta embalagem tem apenas '
                    f'{embalagem.quantidade_actual} {embalagem.unidade} disponíveis.'
                )
            if quantidade <= 0:
                raise forms.ValidationError('A quantidade deve ser maior que zero.')
        
        return cleaned_data
    
class PreferenciasForm(forms.ModelForm):
    """
    Formulário para editar as preferências do utilizador.
    
    Este é um formulário muito simples porque o modelo Preferencias
    só tem um campo editável: dias_alerta_antes.
    """
    
    class Meta:
        model = Preferencias
        fields = ['dias_alerta_antes']
        labels = {
            'dias_alerta_antes': 'Dias de antecedência para alertas',
        }
        widgets = {
            'dias_alerta_antes': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'max': '365',
                'placeholder': 'Ex: 30',
            }),
        }
        help_texts = {
            'dias_alerta_antes': 'Número de dias antes da validade para receber alertas',
        }