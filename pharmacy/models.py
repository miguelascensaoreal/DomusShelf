"""
DomusShelf - Modelos de Dados
=============================
Este ficheiro define a estrutura dos dados que a aplicação vai gerir.
Cada classe representa uma "tabela" na base de dados.

Autor: Miguel Ângelo Ascensão Real
Data: 3 de Fevereiro de 2026
"""

from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Medicamento(models.Model):
    """
    Representa um medicamento no catálogo do utilizador.
    
    Este modelo guarda a informação genérica sobre um medicamento,
    não representa uma caixa física mas sim o "conceito" do medicamento.
    Exemplo: "Ben-u-ron 1g Comprimidos" é um medicamento no catálogo.
    """
    
    # Ligação ao utilizador - cada medicamento pertence a um utilizador
    # on_delete=CASCADE significa: se o utilizador for apagado, os seus medicamentos também são
    utilizador = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='medicamentos',
        verbose_name='Utilizador'
    )
    
    # Nome comercial - o nome que aparece na caixa (ex: "Ben-u-ron", "Brufen")
    nome_comercial = models.CharField(
        max_length=200,
        verbose_name='Nome Comercial'
    )
    
    # Princípio activo - a substância (ex: "Paracetamol", "Ibuprofeno")
    # blank=True significa que pode ficar vazio no formulário
    principio_activo = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Princípio Activo'
    )
    
    # Forma farmacêutica - como o medicamento se apresenta
    # Ex: "Comprimidos", "Xarope", "Pomada", "Gotas"
    forma_farmaceutica = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Forma Farmacêutica'
    )
    
    # Campo para notas adicionais (opcional)
    observacoes = models.TextField(
        blank=True,
        verbose_name='Observações'
    )
    
    # Data de criação - preenchida automaticamente quando o registo é criado
    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
    )
    
    class Meta:
        """Configurações do modelo"""
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'
        # Ordenar alfabeticamente por nome comercial
        ordering = ['nome_comercial']
    
    def __str__(self):
        """
        Define como o medicamento aparece em texto.
        Exemplo: "Ben-u-ron (Paracetamol)"
        """
        if self.principio_activo:
            return f"{self.nome_comercial} ({self.principio_activo})"
        return self.nome_comercial


class Embalagem(models.Model):
    """
    Representa uma unidade física de stock - uma caixa ou frasco concreto.
    
    O mesmo medicamento pode ter várias embalagens com validades diferentes.
    Exemplo: O utilizador pode ter 2 caixas de Ben-u-ron, uma que expira
    em Março e outra em Julho.
    """
    
    # Ligação ao medicamento - cada embalagem pertence a um medicamento
    medicamento = models.ForeignKey(
        Medicamento,
        on_delete=models.CASCADE,
        related_name='embalagens',
        verbose_name='Medicamento'
    )
    
    # Quantidade que vinha originalmente na embalagem
    quantidade_inicial = models.PositiveIntegerField(
        verbose_name='Quantidade Inicial'
    )
    
    # Quantidade que ainda resta (vai diminuindo com os consumos)
    quantidade_actual = models.PositiveIntegerField(
        verbose_name='Quantidade Actual'
    )
    
    # Unidade de medida (ex: "comprimidos", "ml", "gramas", "doses")
    unidade = models.CharField(
        max_length=50,
        default='unidades',
        verbose_name='Unidade'
    )
    
    # Data de validade - apenas a data, sem hora
    data_validade = models.DateField(
        verbose_name='Data de Validade'
    )
    
    # Número do lote (opcional) - útil para rastreabilidade
    lote = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Lote'
    )
    
    # Data de criação do registo
    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
    )
    
    class Meta:
        """Configurações do modelo"""
        verbose_name = 'Embalagem'
        verbose_name_plural = 'Embalagens'
        # FEFO: First Expired, First Out - ordenar por validade (mais antigas primeiro)
        ordering = ['data_validade']
    
    def __str__(self):
        """
        Define como a embalagem aparece em texto.
        Exemplo: "Ben-u-ron - Validade: 2026-03-15 (20 comprimidos)"
        """
        lote_info = f" - Lote: {self.lote}" if self.lote else ""
        return f"{self.medicamento.nome_comercial} - Validade: {self.data_validade}{lote_info} ({self.quantidade_actual} {self.unidade})"
    
    @property
    def esta_expirada(self):
        """
        Verifica se a embalagem já passou da validade.
        Retorna True se já expirou, False caso contrário.
        
        @property permite usar isto como se fosse um atributo:
        embalagem.esta_expirada em vez de embalagem.esta_expirada()
        """
        return date.today() > self.data_validade
    
    @property
    def dias_para_expirar(self):
        """
        Calcula quantos dias faltam para a validade.
        Retorna um número negativo se já expirou.
        """
        delta = self.data_validade - date.today()
        return delta.days


class Consumo(models.Model):
    """
    Regista cada vez que o utilizador toma ou usa um medicamento.
    
    Cada consumo está ligado a uma embalagem específica.
    Quando o consumo é registado, a quantidade_actual da embalagem
    deve ser actualizada (isto será feito nas views).
    """
    
    # Ligação à embalagem de onde foi consumido
    embalagem = models.ForeignKey(
        Embalagem,
        on_delete=models.CASCADE,
        related_name='consumos',
        verbose_name='Embalagem'
    )
    
    # Quantidade que foi consumida
    quantidade = models.PositiveIntegerField(
        verbose_name='Quantidade'
    )
    
    # Data e hora do consumo
    data_hora = models.DateTimeField(
        verbose_name='Data e Hora'
    )
    
    # Observações opcionais (ex: "Tomei com o pequeno-almoço")
    observacoes = models.TextField(
        blank=True,
        verbose_name='Observações'
    )
    
    class Meta:
        """Configurações do modelo"""
        verbose_name = 'Consumo'
        verbose_name_plural = 'Consumos'
        # Ordenar por data, mais recentes primeiro
        ordering = ['-data_hora']
    
    def __str__(self):
        """
        Define como o consumo aparece em texto.
        Exemplo: "2 comprimidos de Ben-u-ron em 03/02/2026"
        """
        return f"{self.quantidade} {self.embalagem.unidade} de {self.embalagem.medicamento.nome_comercial} em {self.data_hora.strftime('%d/%m/%Y')}"


class Preferencias(models.Model):
    """
    Armazena as preferências/configurações de cada utilizador.
    
    Cada utilizador tem exactamente UM registo de preferências.
    A relação OneToOneField garante isto.
    """
    
    # Ligação ao utilizador - relação um-para-um
    utilizador = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='preferencias',
        verbose_name='Utilizador'
    )
    
    # Quantos dias antes da validade o utilizador quer ser alertado
    # Exemplo: 30 significa "alertar quando faltarem 30 dias ou menos"
    dias_alerta_antes = models.PositiveIntegerField(
        default=30,
        verbose_name='Dias de Alerta Antes da Validade'
    )
    
    class Meta:
        """Configurações do modelo"""
        verbose_name = 'Preferências'
        verbose_name_plural = 'Preferências'
    
    def __str__(self):
        """
        Define como as preferências aparecem em texto.
        """
        return f"Preferências de {self.utilizador.username}"