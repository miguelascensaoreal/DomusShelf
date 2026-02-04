# DomusShelf - Ficheiro de Contexto para Continuação do Projecto

**Data de criação deste documento:** 2 de Fevereiro de 2026  
**Última actualização:** 4 de Fevereiro de 2026 (após Fase 7)  
**Objectivo:** Servir como ponto de partida para novos chats de desenvolvimento

---

## INFORMAÇÃO DO ALUNO

- **Nome:** Miguel Ângelo Ascensão Real
- **Número:** 48891
- **Universidade:** UMAIA (Universidade da Maia)
- **Curso:** Mestrado em Informática
- **Disciplina:** Arquitectura e Desenho de Software
- **Professor:** Alexandre Sousa

---

## CONTEXTO DO PROJECTO

### O Que É o DomusShelf

Uma aplicação web para gestão de farmácia doméstica que permite:
- Registar medicamentos que o utilizador tem em casa
- Controlar stock por embalagem/lote com quantidades
- Receber alertas sobre medicamentos prestes a expirar
- Registar consumos que actualizam automaticamente o stock

### Problema Real que Resolve

A acumulação de medicamentos com diferentes datas de validade leva ao desperdício e, em casos graves, ao consumo de medicamentos fora de prazo. Esta app ajuda a gerir a "farmácia caseira" de forma organizada.

---

## REQUISITOS DO PROFESSOR (Enunciado)

Para nota positiva, a aplicação TEM de:

1. ✅ Ter objectivos e complexidade mínima (validado pelo professor)
2. ⬜ Ter documento que descreve a arquitectura (Guião - já aprovado, pode precisar actualização)
3. ⬜ Ter manual de utilizador
4. ✅ Funcionar minimamente (CRUD medicamentos, embalagens, consumos funcionais)
5. ✅ Armazenar dados em base de dados (SQLite com tabelas criadas)
6. ✅ Código fonte em controlo de versões (Git)
7. ✅ Código fonte no GitHub (repositório privado)
8. ⬜ README no GitHub a explicar como operacionalizar

**Nota importante do professor:** "O principal é perceber de Django" — recomendou o Django Girls Tutorial como referência.

---

## DECISÕES TÉCNICAS APROVADAS

| Aspecto | Decisão | Justificação |
|---------|---------|--------------|
| Linguagem | Python 3.12 | Aprovado pelo professor; já instalado no Mac |
| Framework | Django 4.2.27 | "Batteries included"; recomendado pelo professor |
| Base de Dados | SQLite | Zero configuração; portável; adequado para MVP |
| Frontend | Bootstrap 5 via CDN | Responsivo; mobile-first; sem instalação |
| Ícones | Bootstrap Icons via CDN | Conjunto completo de ícones gratuitos |
| Fonte | Inter (Google Fonts) | Moderna, legível, gratuita |
| Tema Visual | Fundo branco, acentos vermelho escuro (#8B0000) | Preferência do aluno |
| Logótipo | Emoji 💊 (pílula) | Simples, fácil de alterar depois |
| Utilizadores | Multi-user com Django Auth | Professor confirmou que Django facilita isto |
| Alertas | Apenas in-app (sino com badge) | Sem emails no MVP |

---

## ESTADO ACTUAL DO PROJECTO

### Fases Concluídas

**Fase 0: Limpeza do Repositório** ✅ (3 de Fevereiro de 2026)
- Ficheiro `.gitignore` criado e configurado
- Pasta `venv/` removida do Git (continua a existir localmente)
- Ficheiro `.DS_Store` removido do Git
- Repositório GitHub limpo e profissional

**Fase 1: Modelos de Dados** ✅ (3 de Fevereiro de 2026)
- Quatro modelos implementados em `pharmacy/models.py`
- Modelos registados no Django Admin em `pharmacy/admin.py`
- Migrações criadas e aplicadas
- Superutilizador criado (username: miguel)
- Dados de teste inseridos

**Fase 2: Autenticação** ✅ (3 de Fevereiro de 2026)
- URLs de autenticação configuradas em `domusshelf_project/urls.py`
- Pasta `templates/registration/` criada
- Template `login.html` criado com design personalizado (vermelho escuro, Bootstrap 5)
- Configuração de `TEMPLATES` em settings.py para encontrar os templates
- Configuração de `LOGIN_URL`, `LOGIN_REDIRECT_URL` e `LOGOUT_REDIRECT_URL`
- Login e logout testados e funcionais

**Fase 3: Template Base e Navegação** ✅ (3 de Fevereiro de 2026)
- Template `templates/base.html` criado com:
  - Bootstrap 5 CSS e JS via CDN
  - Bootstrap Icons via CDN
  - Google Fonts (fonte Inter)
  - Navbar responsiva com menu hamburger para mobile
  - Esquema de cores vermelho escuro (#8B0000)
  - Logótipo com emoji 💊
  - Sino de alertas com badge dinâmico
  - Dropdown de utilizador com Preferências, Administração e Sair
  - Footer com copyright
  - Blocos para herança de templates (title, content, extra_css, extra_js)
- Dashboard inicial criado (`pharmacy/templates/pharmacy/dashboard.html`)
- View `dashboard` criada em `pharmacy/views.py` com decorador `@login_required`
- Responsividade testada (Safari Responsive Design Mode)

**Fase 4: CRUD Medicamentos** ✅ (3 de Fevereiro de 2026)
- Ficheiro `pharmacy/urls.py` criado com namespace `pharmacy`
- Ficheiro `pharmacy/forms.py` criado com `MedicamentoForm` (ModelForm)
- Quatro views implementadas: lista, criar, editar, eliminar
- Três templates criados: lista, form, confirmar eliminar
- Segurança: filtro por `utilizador=request.user` em todas as views

**Fase 5: CRUD Embalagens** ✅ (3 de Fevereiro de 2026)
- URLs de embalagens adicionadas a `pharmacy/urls.py` (prefixo `stock/`)
- `EmbalagemForm` criado com dropdown de medicamentos filtrado por utilizador
- Quatro views implementadas com ordenação FEFO (First Expired First Out)
- Indicadores visuais: vermelho (expirado), amarelo (≤30 dias), verde (OK)
- Optimização com `select_related`

**Fase 6: Registo de Consumos** ✅ (4 de Fevereiro de 2026)
- `ConsumoForm` criado em `pharmacy/forms.py` com:
  - Dropdown de embalagens filtrado por utilizador
  - Apenas embalagens com stock > 0 aparecem no dropdown
  - Validação personalizada no método `clean()` para verificar quantidade disponível
- View `consumo_criar` implementada em `pharmacy/views.py`:
  - Define `data_hora` automaticamente com `timezone.now()`
  - Desconta automaticamente a quantidade da embalagem
  - Redireciona para lista de embalagens após sucesso
- Template `consumo_form.html` criado
- URL `consumo/novo/` adicionada ao `pharmacy/urls.py`
- Links actualizados na navbar e dashboard

**Fase 7: Dashboard e Alertas** ✅ (4 de Fevereiro de 2026)
- Context processor criado (`pharmacy/context_processors.py`):
  - Função `alertas_count()` calcula embalagens expiradas e a expirar
  - Usa preferências do utilizador para dias de antecedência (default: 30)
  - Disponibiliza `alertas_count` em todos os templates automaticamente
- Context processor registado em `settings.py` na secção `TEMPLATES`
- View `dashboard` melhorada com estatísticas reais:
  - Total de medicamentos no catálogo
  - Total de embalagens activas (com stock > 0)
  - Contagem de expiradas e a expirar
- View `alertas_lista` criada para página dedicada de alertas:
  - Separa embalagens em duas secções: expiradas e a expirar
  - Ordenadas por data de validade
- Template `alertas_lista.html` criado com tabelas Bootstrap
- Template `dashboard.html` actualizado com dados dinâmicos
- URL `alertas/` adicionada ao `pharmacy/urls.py`
- Badge do sino na navbar agora mostra contagem real de alertas
- Links do sino actualizados para usar `{% url %}`

### Estrutura Actual do Projecto

```
DomusShelf/
├── docs/                       # Documentação do projecto
│   ├── ARRANCAR_PROJECTO.md
│   ├── CONTEXTO_DOMUSSHELF.md
│   └── REGISTO_DESENVOLVIMENTO.md
├── domusshelf_project/         # Configuração central Django
│   ├── __init__.py
│   ├── settings.py             # ✅ TEMPLATES, LOGIN_URL, context_processors
│   ├── urls.py                 # ✅ URLs de auth + dashboard + include pharmacy
│   ├── asgi.py
│   └── wsgi.py
├── pharmacy/                   # App principal
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py     # ✅ Migração dos modelos
│   ├── templates/pharmacy/     # ✅ Templates específicos da app
│   │   ├── dashboard.html
│   │   ├── medicamento_lista.html
│   │   ├── medicamento_form.html
│   │   ├── medicamento_confirmar_eliminar.html
│   │   ├── embalagem_lista.html
│   │   ├── embalagem_form.html
│   │   ├── embalagem_confirmar_eliminar.html
│   │   ├── consumo_form.html
│   │   └── alertas_lista.html
│   ├── __init__.py
│   ├── admin.py                # ✅ Configuração do Admin
│   ├── apps.py
│   ├── context_processors.py   # ✅ NOVO: alertas_count para todas as páginas
│   ├── forms.py                # ✅ MedicamentoForm + EmbalagemForm + ConsumoForm
│   ├── models.py               # ✅ 4 modelos implementados
│   ├── tests.py
│   ├── urls.py                 # ✅ URLs da app com namespace
│   └── views.py                # ✅ Dashboard + CRUDs + consumos + alertas
├── templates/                  # ✅ Templates globais
│   ├── base.html               # ✅ Template base com navbar e badge dinâmico
│   └── registration/
│       └── login.html          # ✅ Página de login personalizada
├── venv/                       # Ambiente virtual (não está no Git)
├── .gitignore                  # ✅ Configurado
├── db.sqlite3                  # Base de dados com tabelas criadas
├── manage.py
├── requirements.txt
└── README.md                   # Básico, precisa ser expandido
```

### GitHub

- **URL:** https://github.com/miguelascensaoreal/DomusShelf
- **Último commit:** "Implementa dashboard dinâmico e sistema de alertas (Fase 7)"

### Base de Dados

As seguintes tabelas foram criadas e estão funcionais:
- `pharmacy_medicamento` — catálogo de medicamentos
- `pharmacy_embalagem` — stock físico com validades
- `pharmacy_consumo` — registo de tomas
- `pharmacy_preferencias` — configurações do utilizador
- Tabelas do Django Auth (users, groups, permissions, sessions, etc.)

### Utilizadores Criados

| Username | Tipo | Password | Notas |
|----------|------|----------|-------|
| miguel | Superuser | (definida pelo aluno) | Para desenvolvimento |
| professor | (a criar) | demo2026 | Para demonstração ao professor |

### Dados de Teste

Medicamentos criados:
- Ben-u-ron 1gr (Paracetamol), Comprimidos
- Brufen 400mg (Ibuprofeno), Comprimidos

Embalagens criadas:
- Ben-u-ron: 20 comprimidos, validade 30/11/2028, lote 619K241 (OK)
- Brufen: 18 comprimidos (após consumos), validade 20/02/2026, lote ABC321 (a expirar em breve)

---

## MODELO DE DADOS IMPLEMENTADO

### Entidades

```
MEDICAMENTO (catálogo)
├── id (PK, auto)
├── utilizador (FK → User)      # Para multi-user
├── nome_comercial (string)     # Ex: "Ben-u-ron"
├── principio_activo (string)   # Ex: "Paracetamol"
├── forma_farmaceutica (string) # Ex: "Comprimidos"
├── observacoes (text, opcional)
└── criado_em (datetime, auto)

EMBALAGEM (stock físico)
├── id (PK, auto)
├── medicamento (FK → Medicamento)
├── quantidade_inicial (int)
├── quantidade_actual (int)     # Decrementada pelos consumos
├── unidade (string)            # Ex: "comprimidos", "ml"
├── data_validade (date)        # Só data, sem hora
├── lote (string, opcional)
└── criado_em (datetime, auto)

CONSUMO (registo de tomas)
├── id (PK, auto)
├── embalagem (FK → Embalagem)
├── quantidade (int)
├── data_hora (datetime)
└── observacoes (text, opcional)

PREFERENCIAS (configuração por utilizador)
├── id (PK, auto)
├── utilizador (FK → User, OneToOne)
└── dias_alerta_antes (int, default=30)
```

### Relações
- User 1:N Medicamento (cada utilizador tem os seus medicamentos)
- Medicamento 1:N Embalagem
- Embalagem 1:N Consumo
- User 1:1 Preferencias

### Regras de Negócio Implementadas
- Ordenação de embalagens: por data_validade ASC (FEFO - First Expired First Out)
- Propriedade `esta_expirada`: verifica se a embalagem já passou da validade
- Propriedade `dias_para_expirar`: calcula quantos dias faltam para a validade
- Consumos descontam automaticamente da `quantidade_actual` da embalagem
- Validação impede consumir mais do que a quantidade disponível

---

## FUNCIONALIDADES DO MVP

| ID | Funcionalidade | Descrição | Estado |
|----|----------------|-----------|--------|
| F1 | Gestão de Medicamentos | CRUD completo do catálogo | ✅ Concluído |
| F2 | Gestão de Embalagens | CRUD com ordenação FEFO | ✅ Concluído |
| F3 | Registo de Consumos | Formulário + desconto automático | ✅ Concluído |
| F4 | Sistema de Alertas | Sino com badge + página de alertas | ✅ Concluído |
| F5 | Dashboard | Visão geral + estatísticas reais | ✅ Concluído |
| F6 | Preferências | Configurar dias de alerta | ⬜ Pendente |
| F7 | Autenticação | Login/Logout (Django built-in) | ✅ Concluído |
| F8 | Registo de Utilizador | Criar conta nova | ⬜ Opcional |

---

## PLANO DE IMPLEMENTAÇÃO (Fases)

### Fases Concluídas ✅

- Fase 0: Limpeza e Preparação
- Fase 1: Modelos de Dados
- Fase 2: Autenticação
- Fase 3: Template Base e Navegação
- Fase 4: CRUD Medicamentos
- Fase 5: CRUD Embalagens
- Fase 6: Registo de Consumos
- Fase 7: Dashboard e Alertas

### Fase 8: Preferências ⬜ PRÓXIMA
**Tempo estimado:** 30 minutos
- [ ] Criar `PreferenciasForm` em `pharmacy/forms.py`
- [ ] Criar view `preferencias_editar` para página de preferências
- [ ] Criar template `preferencias_form.html`
- [ ] Criar Preferencias automaticamente para novos utilizadores (signal ou na view)
- [ ] Adicionar URL `preferencias/`
- [ ] Actualizar link "Configurar" no dashboard
- [ ] Commit e push

### Fase 9: Polimento Final ⬜
**Tempo estimado:** 1-2 horas
- [ ] Criar fixtures com dados de exemplo
- [ ] Actualizar README.md com instruções completas
- [ ] Criar utilizador demo: username=`professor`, password=`demo2026`
- [ ] Testar instalação do zero (simular ser o professor)
- [ ] Actualizar documento de arquitectura se necessário
- [ ] Criar manual de utilizador básico
- [ ] Commit final e push

---

## COMANDOS ÚTEIS

```bash
# Navegar para a pasta do projecto
cd ~/Documents/DomusShelf

# Activar ambiente virtual (SEMPRE antes de trabalhar)
source venv/bin/activate

# Verificar que está activado (deve mostrar (venv) no início)
which python

# Correr servidor de desenvolvimento
python manage.py runserver

# Parar servidor
Control + C

# Criar migrações após alterar models.py
python manage.py makemigrations

# Aplicar migrações à base de dados
python manage.py migrate

# Criar superuser para aceder ao Admin
python manage.py createsuperuser

# Aceder ao Django Admin
# Abrir browser em: http://127.0.0.1:8000/admin/

# Ver estado do Git
git status

# Adicionar ficheiros ao commit
git add .

# Fazer commit
git commit -m "Mensagem descritiva"

# Enviar para GitHub
git push origin main

# Carregar fixtures (dados de exemplo)
python manage.py loaddata nome_do_ficheiro.json
```

---

## URLs IMPLEMENTADAS

| URL | Função | Estado |
|-----|--------|--------|
| `/` | Dashboard (página inicial) | ✅ Funcional |
| `/admin/` | Painel de administração Django | ✅ Funcional |
| `/accounts/login/` | Página de login | ✅ Funcional |
| `/accounts/logout/` | Logout (redireciona para login) | ✅ Funcional |
| `/medicamentos/` | Lista do catálogo | ✅ Funcional |
| `/medicamentos/novo/` | Formulário criação | ✅ Funcional |
| `/medicamentos/<id>/editar/` | Formulário edição | ✅ Funcional |
| `/medicamentos/<id>/eliminar/` | Confirmação eliminação | ✅ Funcional |
| `/medicamentos/stock/` | Lista de embalagens (FEFO) | ✅ Funcional |
| `/medicamentos/stock/nova/` | Adicionar embalagem | ✅ Funcional |
| `/medicamentos/stock/<id>/editar/` | Editar embalagem | ✅ Funcional |
| `/medicamentos/stock/<id>/eliminar/` | Eliminar embalagem | ✅ Funcional |
| `/medicamentos/consumo/novo/` | Registar toma | ✅ Funcional |
| `/medicamentos/alertas/` | Lista de alertas | ✅ Funcional |

## URLs A IMPLEMENTAR (Fases seguintes)

| URL | Função | Fase |
|-----|--------|------|
| `/medicamentos/preferencias/` | Configuração | Fase 8 |

---

## CONCEITOS DJANGO APRENDIDOS

### Fases 1-5 (sessões anteriores)
- Herança de Templates (`{% extends %}` e `{% block %}`)
- Decorador `@login_required`
- Variável `{{ user }}` em templates
- Responsividade Bootstrap
- URLs com Namespaces (`app_name`)
- Path Converters (`<int:pk>`)
- ModelForms
- Padrão GET/POST nas Views
- `commit=False` para modificar antes de guardar
- `get_object_or_404`
- Filtrar por relação com `__` (double underscore)
- `select_related` para optimização

### Fase 6: Registo de Consumos (4 de Fevereiro de 2026)

**Validação Personalizada com `clean()`**
O método `clean()` num ModelForm permite adicionar regras de validação próprias. No `ConsumoForm`, usamos para verificar se a quantidade a consumir não excede a quantidade disponível:
```python
def clean(self):
    cleaned_data = super().clean()
    embalagem = cleaned_data.get('embalagem')
    quantidade = cleaned_data.get('quantidade')
    if embalagem and quantidade:
        if quantidade > embalagem.quantidade_actual:
            raise forms.ValidationError('Quantidade indisponível...')
    return cleaned_data
```

**timezone.now() vs datetime.now()**
O Django recomenda usar `from django.utils import timezone` e `timezone.now()` em vez de `datetime.now()`. Isto garante que as datas/horas são tratadas correctamente com fusos horários (timezone-aware).

**Actualização de Objectos Relacionados**
Ao registar um consumo, precisamos de actualizar a embalagem associada:
```python
embalagem = consumo.embalagem
embalagem.quantidade_actual -= consumo.quantidade
embalagem.save()  # Guardar a embalagem
consumo.save()    # Guardar o consumo
```

### Fase 7: Dashboard e Alertas (4 de Fevereiro de 2026)

**Context Processors**
São funções que adicionam variáveis ao contexto de TODOS os templates automaticamente. Úteis para dados que aparecem em todas as páginas, como a contagem de alertas no sino.

Ficheiro `pharmacy/context_processors.py`:
```python
def alertas_count(request):
    if not request.user.is_authenticated:
        return {'alertas_count': 0}
    # ... lógica de contagem ...
    return {'alertas_count': count}
```

Registo em `settings.py`:
```python
TEMPLATES = [{
    'OPTIONS': {
        'context_processors': [
            # ... outros ...
            'pharmacy.context_processors.alertas_count',
        ],
    },
}]
```

**Filtros de Data com timedelta**
Para calcular datas futuras (ex: 30 dias a partir de hoje):
```python
from datetime import date, timedelta
hoje = date.today()
data_limite = hoje + timedelta(days=30)
```

**Queries com Comparações de Datas**
O Django ORM permite comparar datas facilmente:
- `data_validade__lt=hoje` — validade menor que hoje (expirado)
- `data_validade__lte=data_limite` — validade menor ou igual ao limite
- `data_validade__gte=hoje` — validade maior ou igual a hoje (ainda válido)

**Try/Except para Objectos que Podem Não Existir**
Quando um objecto pode não existir na base de dados:
```python
try:
    prefs = Preferencias.objects.get(utilizador=request.user)
    dias_alerta = prefs.dias_alerta_antes
except Preferencias.DoesNotExist:
    dias_alerta = 30  # Valor por defeito
```

---

## FICHEIROS DE DOCUMENTAÇÃO

| Ficheiro | Localização | Propósito |
|----------|-------------|-----------|
| CONTEXTO_DOMUSSHELF.md | docs/ (e anexar a cada chat) | Contexto para continuar o desenvolvimento |
| ARRANCAR_PROJECTO.md | docs/ | Instruções para iniciar o ambiente |
| REGISTO_DESENVOLVIMENTO.md | docs/ | Histórico para o relatório académico |

---

## HISTÓRICO DE SESSÕES

### Sessão 1 — 18 de Janeiro de 2026
- Configuração inicial do ambiente de desenvolvimento
- Instalação do Python 3.12 e Django 4.2.27
- Criação do projecto Django e app pharmacy
- Setup do repositório GitHub
- Explicação detalhada dos conceitos (Git, venv, Django)

### Sessão 2 — 2 de Fevereiro de 2026
- Revisão do estado do projecto
- Confirmação das decisões técnicas
- Planeamento das fases de implementação
- Criação do ficheiro CONTEXTO_DOMUSSHELF.md

### Sessão 3 — 3 de Fevereiro de 2026
- **Fase 0 concluída:** Limpeza do repositório
- **Fase 1 concluída:** Implementação dos 4 modelos de dados
- **Fase 2 concluída:** Sistema de autenticação
- **Fase 3 concluída:** Template base com navbar responsiva

### Sessão 4 — 3 de Fevereiro de 2026
- **Fase 4 concluída:** CRUD completo de medicamentos
- **Fase 5 concluída:** CRUD completo de embalagens

### Sessão 5 — 4 de Fevereiro de 2026
- Resolução de problema com ambiente virtual corrompido (recriação do venv)
- **Fase 6 concluída:** Registo de consumos com desconto automático de stock
  - ConsumoForm com validação personalizada
  - View consumo_criar com timezone.now()
  - Template consumo_form.html
- **Fase 7 concluída:** Dashboard dinâmico e sistema de alertas
  - Context processor para contagem de alertas em todas as páginas
  - Dashboard com estatísticas reais
  - Página dedicada de alertas (expiradas + a expirar)
  - Badge dinâmico no sino da navbar

---

## PRÓXIMA SESSÃO

**Começar por:** Fase 8 (Preferências)

**Primeiro comando a executar:**
```bash
cd ~/Documents/DomusShelf
source venv/bin/activate
python manage.py runserver
```

**Verificar que funciona:** Aceder a http://127.0.0.1:8000/ e confirmar que o dashboard mostra estatísticas

**Tarefas da Fase 8:**
- Criar PreferenciasForm em `pharmacy/forms.py`
- Criar view `preferencias_editar` 
- Criar template `preferencias_form.html`
- Adicionar URL e actualizar links
- Criar objecto Preferencias automaticamente se não existir

**Conceitos novos esperados:**
- `get_or_create()` para criar objecto se não existir
- Formulário simples de configuração

---

## NOTAS IMPORTANTES

### Estilo de Documentos
- Português de Portugal sem novo acordo ortográfico
- Todos os documentos para entrega devem ter disclaimer sobre uso de IA
- Formato do disclaimer: "Foi utilizada uma LLM (Claude AI) como ferramenta de apoio, não para realização de trabalho completo."

### Commits
- Fazer commits frequentes com mensagens descritivas em português
- Exemplo: "Implementa dashboard dinâmico e sistema de alertas (Fase 7)"

### Problemas Conhecidos Resolvidos
- **Ambiente virtual corrompido:** Se o venv deixar de funcionar após actualizações do macOS/Homebrew, apagar e recriar com `rm -rf venv && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt`
- **Erros de favicon.ico:** São inofensivos, apenas o browser a pedir um ícone que não existe
- **Import de Preferencias:** É um modelo, não um formulário. Importar de `.models`, não de `.forms`

---

## CREDENCIAIS

| Ambiente | Username | Password | Notas |
|----------|----------|----------|-------|
| Django Admin (dev) | miguel | (definida pelo aluno) | Superuser para desenvolvimento |
| Django Admin (demo) | professor | demo2026 | A criar na Fase 9 |

---

## LINKS ÚTEIS

- **Repositório GitHub:** https://github.com/miguelascensaoreal/DomusShelf
- **Django Documentation:** https://docs.djangoproject.com/
- **Django Girls Tutorial (PT):** https://tutorial.djangogirls.org/pt/
- **Bootstrap 5 Docs:** https://getbootstrap.com/docs/5.3/
- **Bootstrap Icons:** https://icons.getbootstrap.com/

---

*Este ficheiro deve ser anexado ao início de cada novo chat para manter o contexto do projecto.*
