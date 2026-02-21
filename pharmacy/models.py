"""
DomusShelf - Modelos de Dados
=============================
Este ficheiro define a estrutura dos dados que a aplicação vai gerir.
Cada classe representa uma "tabela" na base de dados.

Autor: Miguel Ângelo Ascensão Real
Data: 3 de Fevereiro de 2026
Actualizado: Fevereiro de 2026 (v2 — Conceito de Família)
"""

from django.db import models
from django.contrib.auth.models import User
from datetime import date
import uuid


# =============================================================================
# Manager customizado para Soft Delete
# =============================================================================

class SoftDeleteManager(models.Manager):
    """
    Manager que filtra automaticamente registos marcados como eliminados.
    Todas as queries normais (Model.objects.all(), .filter(), etc.) só
    devolvem registos NÃO eliminados. Para ver tudo, usa-se Model.all_objects.
    
    Analogia: é como um caixote do lixo — os itens ainda existem, mas não
    aparecem na prateleira. Só quem abrir o caixote os vê.
    """
    def get_queryset(self):
        return super().get_queryset().filter(eliminado_em__isnull=True)


# =============================================================================
# Modelo Familia (NOVO na v2)
# =============================================================================

class Familia(models.Model):
    """
    Representa uma unidade familiar que partilha o mesmo armário de medicamentos.
    
    Na v1, cada utilizador vivia isolado. Na v2, os utilizadores podem agrupar-se
    numa Família, partilhando catálogo e stock. Quem cria a Família é o Super User.
    """
    nome = models.CharField(
        max_length=100,
        verbose_name='Nome da Família'
    )
    
    # O utilizador que criou e gere a família
    super_user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        related_name='familia_gerida',
        verbose_name='Super User'
    )
    
    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
    )
    
    # Soft delete
    eliminado_em = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Eliminado em'
    )
    
    # Managers
    objects = SoftDeleteManager()
    all_objects = models.Manager()
    
    class Meta:
        verbose_name = 'Família'
        verbose_name_plural = 'Famílias'
        ordering = ['nome']
    
    def __str__(self):
        return self.nome


# =============================================================================
# Modelos existentes (actualizados para v2)
# =============================================================================

class Medicamento(models.Model):
    """
    Representa um medicamento no catálogo.
    
    v2: O medicamento pertence a uma Família (se o utilizador tiver uma).
    Utilizadores sem família mantêm o comportamento da v1.
    """
    utilizador = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='medicamentos',
        verbose_name='Utilizador'
    )
    
    # NOVO v2 — Família a que pertence (null = modo individual v1)
    familia = models.ForeignKey(
        Familia,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='medicamentos',
        verbose_name='Família'
    )
    
    nome_comercial = models.CharField(
        max_length=200,
        verbose_name='Nome Comercial'
    )
    
    principio_activo = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Princípio Activo'
    )
    
    forma_farmaceutica = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Forma Farmacêutica'
    )
    
    observacoes = models.TextField(
        blank=True,
        verbose_name='Observações'
    )
    
    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
    )
    
    # NOVO v2 — Soft delete
    eliminado_em = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Eliminado em'
    )
    
    # Managers
    objects = SoftDeleteManager()
    all_objects = models.Manager()
    
    class Meta:
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'
        ordering = ['nome_comercial']
    
    def __str__(self):
        if self.principio_activo:
            return f"{self.nome_comercial} ({self.principio_activo})"
        return self.nome_comercial


class Embalagem(models.Model):
    """
    Representa uma unidade física de stock - uma caixa ou frasco concreto.
    """
    medicamento = models.ForeignKey(
        Medicamento,
        on_delete=models.CASCADE,
        related_name='embalagens',
        verbose_name='Medicamento'
    )
    
    quantidade_inicial = models.PositiveIntegerField(
        verbose_name='Quantidade Inicial'
    )
    
    quantidade_actual = models.PositiveIntegerField(
        verbose_name='Quantidade Actual'
    )
    
    unidade = models.CharField(
        max_length=50,
        default='unidades',
        verbose_name='Unidade'
    )
    
    data_validade = models.DateField(
        verbose_name='Data de Validade'
    )
    
    lote = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Lote'
    )
    
    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
    )
    
    # NOVO v2 — Soft delete
    eliminado_em = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Eliminado em'
    )
    
    # Managers
    objects = SoftDeleteManager()
    all_objects = models.Manager()
    
    class Meta:
        verbose_name = 'Embalagem'
        verbose_name_plural = 'Embalagens'
        ordering = ['data_validade']
    
    def __str__(self):
        lote_info = f" - Lote: {self.lote}" if self.lote else ""
        return (
            f"{self.medicamento.nome_comercial} - "
            f"Validade: {self.data_validade}{lote_info} "
            f"({self.quantidade_actual} {self.unidade})"
        )
    
    @property
    def esta_expirada(self):
        return date.today() > self.data_validade
    
    @property
    def dias_para_expirar(self):
        delta = self.data_validade - date.today()
        return delta.days


class Consumo(models.Model):
    """
    Regista cada vez que alguém toma ou usa um medicamento.
    
    v2: O consumo fica associado ao utilizador que o registou,
    permitindo rastreio individual mesmo em contexto de família.
    """
    embalagem = models.ForeignKey(
        Embalagem,
        on_delete=models.CASCADE,
        related_name='consumos',
        verbose_name='Embalagem'
    )
    
    # NOVO v2 — Quem consumiu (antes era implícito via embalagem→medicamento→user)
    utilizador = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='consumos',
        verbose_name='Consumido por'
    )
    
    quantidade = models.PositiveIntegerField(
        verbose_name='Quantidade'
    )
    
    data_hora = models.DateTimeField(
        verbose_name='Data e Hora'
    )
    
    observacoes = models.TextField(
        blank=True,
        verbose_name='Observações'
    )
    
    # NOVO v2 — Campos para anulação de consumos (F13)
    anulado = models.BooleanField(
        default=False,
        verbose_name='Anulado'
    )
    
    anulado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='consumos_anulados',
        verbose_name='Anulado por'
    )
    
    anulado_em = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Anulado em'
    )
    
    motivo_anulacao = models.TextField(
        blank=True,
        verbose_name='Motivo da Anulação'
    )
    
    class Meta:
        verbose_name = 'Consumo'
        verbose_name_plural = 'Consumos'
        ordering = ['-data_hora']
    
    def __str__(self):
        return (
            f"{self.quantidade} {self.embalagem.unidade} de "
            f"{self.embalagem.medicamento.nome_comercial} em "
            f"{self.data_hora.strftime('%d/%m/%Y')}"
        )


class Preferencias(models.Model):
    """
    Armazena as preferências/configurações de cada utilizador.
    
    v2: Inclui referência à família a que o utilizador pertence.
    """
    utilizador = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='preferencias',
        verbose_name='Utilizador'
    )
    
    # NOVO v2 — Família a que pertence
    familia = models.ForeignKey(
        Familia,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='membros',
        verbose_name='Família'
    )
    
    dias_alerta_antes = models.PositiveIntegerField(
        default=30,
        verbose_name='Dias de Alerta Antes da Validade'
    )
    
    # NOVO v2 — Soft delete (para contas eliminadas)
    eliminado_em = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Eliminado em'
    )
    
    class Meta:
        verbose_name = 'Preferências'
        verbose_name_plural = 'Preferências'
    
    def __str__(self):
        return f"Preferências de {self.utilizador.username}"
    
class Convite(models.Model):
    """
    Código de convite para juntar um utilizador a uma família.
    
    O Super User gera um convite, que produz um código alfanumérico único.
    O código tem prazo de validade (48h) e só pode ser usado uma vez.
    
    Analogia: é como um bilhete de entrada com código QR — é único,
    tem prazo, e depois de usado fica invalidado.
    """
    
    familia = models.ForeignKey(
        Familia,
        on_delete=models.CASCADE,
        related_name='convites',
        verbose_name='Família'
    )
    
    # Código alfanumérico de 8 caracteres, gerado automaticamente
    codigo = models.CharField(
        max_length=8,
        unique=True,
        verbose_name='Código de Convite'
    )
    
    # Quem criou o convite (deve ser o Super User)
    criado_por = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='convites_criados',
        verbose_name='Criado por'
    )
    
    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
    )
    
    # Válido por 48 horas a partir da criação
    expira_em = models.DateTimeField(
        verbose_name='Expira em'
    )
    
    # Quem usou o convite (null = ainda não foi usado)
    usado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='convite_usado',
        verbose_name='Usado por'
    )
    
    usado_em = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Usado em'
    )
    
    # O Super User pode revogar um convite antes de ser usado
    revogado = models.BooleanField(
        default=False,
        verbose_name='Revogado'
    )
    
    class Meta:
        verbose_name = 'Convite'
        verbose_name_plural = 'Convites'
        ordering = ['-criado_em']
    
    def __str__(self):
        return f"Convite {self.codigo} para {self.familia.nome}"
    
    @property
    def esta_valido(self):
        """
        Um convite é válido se: não expirou, não foi usado, e não foi revogado.
        """
        from django.utils import timezone
        return (
            not self.revogado
            and self.usado_por is None
            and self.expira_em > timezone.now()
        )
    
    @staticmethod
    def gerar_codigo():
        """
        Gera um código alfanumérico de 8 caracteres, em maiúsculas.
        Usa uuid4 para garantir unicidade e depois encurta.
        """
        return uuid.uuid4().hex[:8].upper()

# =============================================================================
# Modelo RegistoActividade (NOVO na v2 — Fase 13)
# =============================================================================

class RegistoActividade(models.Model):
    """
    Regista cronologicamente todas as acções relevantes numa família.
    Analogia: é o "diário de bordo" da farmácia familiar — cada acção
    fica registada com quem a fez, quando e o que aconteceu.
    
    Apenas famílias têm logbook. Utilizadores sem família não geram registos.
    """
    
    # Tipos de acção possíveis
    TIPO_CHOICES = [
        ('medicamento_criado', 'Medicamento criado'),
        ('medicamento_editado', 'Medicamento editado'),
        ('medicamento_eliminado', 'Medicamento eliminado'),
        ('embalagem_criada', 'Embalagem criada'),
        ('embalagem_editada', 'Embalagem editada'),
        ('embalagem_eliminada', 'Embalagem eliminada'),
        ('consumo_registado', 'Consumo registado'),
        ('convite_gerado', 'Convite gerado'),
        ('convite_aceite', 'Convite aceite'),
        ('convite_revogado', 'Convite revogado'),
        ('membro_removido', 'Membro removido'),
    ]
    
    familia = models.ForeignKey(
        Familia,
        on_delete=models.CASCADE,
        related_name='registos_actividade',
        verbose_name='Família'
    )
    
    utilizador = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='registos_actividade',
        verbose_name='Utilizador'
    )
    
    tipo = models.CharField(
        max_length=50,
        choices=TIPO_CHOICES,
        verbose_name='Tipo de Acção'
    )
    
    descricao = models.TextField(
        verbose_name='Descrição'
    )
    
    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data e Hora'
    )
    
    class Meta:
        verbose_name = 'Registo de Actividade'
        verbose_name_plural = 'Registos de Actividade'
        ordering = ['-criado_em']
    
    def __str__(self):
        return f"[{self.criado_em.strftime('%d/%m/%Y %H:%M')}] {self.utilizador} — {self.get_tipo_display()}"