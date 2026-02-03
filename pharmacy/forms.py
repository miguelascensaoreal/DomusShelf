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
from .models import Medicamento


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
