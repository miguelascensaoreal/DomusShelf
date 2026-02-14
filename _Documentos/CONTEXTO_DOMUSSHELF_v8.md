# DomusShelf - Ficheiro de Contexto para Continuação do Projecto

**Data de criação deste documento:** 2 de Fevereiro de 2026  
**Última actualização:** 13 de Fevereiro de 2026 (Fase 10 concluída — aplicação completa)  
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
2. ✅ Ter documento que descreve a arquitectura (Guião aprovado)
3. ⬜ Ter manual de utilizador
4. ✅ Funcionar minimamente (CRUD completo, alertas, preferências)
5. ✅ Armazenar dados em base de dados (SQLite)
6. ✅ Código fonte em controlo de versões (Git)
7. ✅ Código fonte no GitHub (repositório público)
8. ✅ README no GitHub a explicar como operacionalizar

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
| Date Picker | Flatpickr via CDN | Calendário elegante com suporte a formato português |
| Tema Visual | Fundo branco, acentos vermelho escuro (#8B0000) | Preferência do aluno |
| Logótipo | Emoji 💊 (pílula) | Simples, fácil de alterar depois |
| Utilizadores | Multi-user com Django Auth | Professor confirmou que Django facilita isto |
| Alertas | Apenas in-app (sino com badge) | Sem emails no MVP |
| Localização | Português de Portugal (pt-pt) | Datas em formato dd/mm/aaaa |

---

## ESTADO ACTUAL DO PROJECTO

### Fases Concluídas

**Fase 0: Limpeza do Repositório** ✅ (2 de Fevereiro de 2026)
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

**Fase 8: Preferências** ✅ (4 de Fevereiro de 2026)
- `PreferenciasForm` criado em `pharmacy/forms.py`:
  - Campo `dias_alerta_antes` com widget NumberInput
  - Labels e help_texts em português
- View `preferencias_editar` implementada em `pharmacy/views.py`:
  - Usa `get_or_create()` para criar preferências automaticamente se não existirem
  - Formulário pré-preenchido com valores actuais
  - Redireciona para dashboard após guardar
- Template `preferencias_form.html` criado
- URL `preferencias/` adicionada ao `pharmacy/urls.py`
- Links actualizados no dashboard e na navbar (dropdown do utilizador)
- Corrigido bug: link da navbar usava URL hardcoded `/preferencias/` em vez de `{% url 'pharmacy:preferencias_editar' %}`

**Fase 9: Polimento Final** 🔄 (5 de Fevereiro de 2026 - Em progresso)
- ✅ Utilizador demo criado: `Professor` / `DemoADS2026`
- ✅ Base de dados pré-populada com 10 medicamentos comuns portugueses para ambos os utilizadores (miguel e Professor)
- ✅ README.md actualizado com instruções completas de instalação e operacionalização
- ✅ Configuração de localização portuguesa em `settings.py`:
  - `LANGUAGE_CODE = 'pt-pt'`
  - `TIME_ZONE = 'Europe/Lisbon'`
  - `DATE_INPUT_FORMATS` para aceitar formato dd/mm/aaaa
- ✅ Flatpickr integrado para date picker com calendário visual em formato português
- ⬜ Manual de utilizador
- ⬜ Relatório final

**Fase 10: Melhorias de Usabilidade** ✅ (13 de Fevereiro de 2026)
- Tarefa 10.1: Lote no dropdown de consumos
  - Alterado `__str__()` do modelo Embalagem para incluir número de lote condicionalmente
  - Formato: "Brufen 400mg - Validade: 2026-02-20 - Lote: ABC321 (18 comprimidos)"
- Tarefa 10.2: Registo de novo utilizador
  - View `registo` criada em `pharmacy/views.py` usando `UserCreationForm` do Django
  - Template `registration/registo.html` criado seguindo o design do login
  - URL `accounts/registo/` adicionada em `domusshelf_project/urls.py`
  - Link "Criar conta" adicionado à página de login
  - Mensagem de sucesso exibida no login após registo (Django `messages` framework)
  - Suporte para `messages` adicionado ao template `login.html`

### Estrutura Actual do Projecto

```
DomusShelf/
├── docs/                       # Documentação do projecto
│   ├── ARRANCAR_PROJECTO.md
│   ├── CONTEXTO_DOMUSSHELF.md
│   └── REGISTO_DESENVOLVIMENTO.md
├── domusshelf_project/         # Configuração central Django
│   ├── __init__.py
│   ├── settings.py             # ✅ Localização pt-pt, DATE_INPUT_FORMATS
│   ├── urls.py                 # ✅ URLs de auth + dashboard + registo + include pharmacy
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
│   │   ├── alertas_lista.html
│   │   └── preferencias_form.html  # ✅ NOVO na Fase 8
│   ├── __init__.py
│   ├── admin.py                # ✅ Configuração do Admin
│   ├── apps.py
│   ├── context_processors.py   # ✅ alertas_count para todas as páginas
│   ├── forms.py                # ✅ Medicamento + Embalagem + Consumo + Preferencias
│   ├── models.py               # ✅ 4 modelos implementados
│   ├── tests.py
│   ├── urls.py                 # ✅ URLs da app com namespace
│   └── views.py                # ✅ Dashboard + CRUDs + consumos + alertas + preferências + registo
├── templates/                  # ✅ Templates globais
│   ├── base.html               # ✅ Inclui Flatpickr para date picker
│   └── registration/
│       └── login.html          # ✅ Página de login personalizada (com suporte a messages)
│       └── registo.html        # ✅ Fase 10: Página de registo de novo utilizador
├── venv/                       # Ambiente virtual (não está no Git)
├── .gitignore                  # ✅ Configurado
├── db.sqlite3                  # Base de dados com dados pré-populados
├── manage.py
├── requirements.txt
└── README.md                   # ✅ Instruções completas de operacionalização
```

### GitHub

- **URL:** https://github.com/miguelascensaoreal/DomusShelf
- **Último commit:** "Adiciona Flatpickr para date picker em formato português (dd/mm/aaaa)"

### Base de Dados

As seguintes tabelas foram criadas e estão funcionais:
- `pharmacy_medicamento` — catálogo de medicamentos (10 pré-populados por utilizador)
- `pharmacy_embalagem` — stock físico com validades
- `pharmacy_consumo` — registo de tomas
- `pharmacy_preferencias` — configurações do utilizador
- Tabelas do Django Auth (users, groups, permissions, sessions, etc.)

### Utilizadores Criados

| Username | Tipo | Password | Notas |
|----------|------|----------|-------|
| miguel | Superuser | (definida pelo aluno) | Para desenvolvimento |
| Professor | Superuser | DemoADS2026 | Para demonstração ao professor |

### Dados Pré-Populados (Fase 9)

Os seguintes 10 medicamentos foram criados para ambos os utilizadores:

| Nome Comercial | Princípio Activo | Forma |
|----------------|------------------|-------|
| Ben-u-ron 1g | Paracetamol | Comprimidos |
| Brufen 400mg | Ibuprofeno | Comprimidos |
| Aspirina 500mg | Ácido Acetilsalicílico | Comprimidos |
| Voltaren Emulgel | Diclofenac | Gel |
| Omeprazol 20mg | Omeprazol | Cápsulas |
| Zyrtec 10mg | Cetirizina | Comprimidos |
| Betadine | Iodopovidona | Solução cutânea |
| Strepfen 8.75mg | Flurbiprofeno | Pastilhas |
| Dulcolax 5mg | Bisacodilo | Comprimidos |
| Imodium 2mg | Loperamida | Cápsulas |

**Nota:** As embalagens (stock) devem ser criadas por cada utilizador conforme os medicamentos que realmente possui.

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
- Preferências criadas automaticamente com `get_or_create()` se não existirem

---

## FUNCIONALIDADES DO MVP

| ID | Funcionalidade | Descrição | Estado |
|----|----------------|-----------|--------|
| F1 | Gestão de Medicamentos | CRUD completo do catálogo | ✅ Concluído |
| F2 | Gestão de Embalagens | CRUD com ordenação FEFO e date picker | ✅ Concluído |
| F3 | Registo de Consumos | Formulário + desconto automático | ✅ Concluído |
| F4 | Sistema de Alertas | Sino com badge + página de alertas | ✅ Concluído |
| F5 | Dashboard | Visão geral + estatísticas reais | ✅ Concluído |
| F6 | Preferências | Configurar dias de alerta | ✅ Concluído |
| F7 | Autenticação | Login/Logout (Django built-in) | ✅ Concluído |
| F8 | Registo de Utilizador | Criar conta nova na página de login | ✅ Concluído |
| F9 | Lote no Consumo | Mostrar lote na selecção de embalagem ao registar toma | ✅ Concluído |

---

## CONFIGURAÇÕES DE LOCALIZAÇÃO

As seguintes configurações foram adicionadas ao `settings.py` para suportar o formato português:

```python
# Configuração de idioma e localização
LANGUAGE_CODE = 'pt-pt'
TIME_ZONE = 'Europe/Lisbon'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Formatos de data aceites (o primeiro é o preferido)
DATE_INPUT_FORMATS = [
    '%d/%m/%Y',  # 05/02/2026 (formato português)
    '%d-%m-%Y',  # 05-02-2026
    '%Y-%m-%d',  # 2026-02-05 (formato ISO)
]
```

### Flatpickr (Date Picker)

Integrado via CDN no `base.html` para campos de data com calendário visual:
- CSS: `https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css`
- JS: `https://cdn.jsdelivr.net/npm/flatpickr`
- Localização PT: `https://cdn.jsdelivr.net/npm/flatpickr/dist/l10n/pt.js`

Configuração JavaScript:
```javascript
flatpickr('.datepicker', {
    dateFormat: 'd/m/Y',
    altInput: true,
    altFormat: 'd/m/Y',
    locale: 'pt',
    allowInput: true,
});
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
| `/medicamentos/preferencias/` | Configuração de alertas | ✅ Funcional |
| `/accounts/registo/` | Página de registo de novo utilizador | ✅ Funcional |

---

## CONCEITOS DJANGO EXPLICADOS E APRENDIDOS

### Fases 1-7 (sessões anteriores)
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
- Context Processors
- Filtros de data com `timedelta`
- Queries com comparações de datas (`__lt`, `__lte`, `__gte`)
- `try/except` para objectos que podem não existir
- Validação personalizada com `clean()` em ModelForms
- `timezone.now()` vs `datetime.now()`

### Fase 8: Preferências (4 de Fevereiro de 2026)

**get_or_create()**
Método do Django ORM que tenta obter um objecto; se não existir, cria-o automaticamente. Retorna uma tupla `(objecto, foi_criado)`:
```python
preferencias, criado = Preferencias.objects.get_or_create(
    utilizador=request.user,
    defaults={'dias_alerta_antes': 30}
)
```
- Os campos fora de `defaults` são usados para procurar E para criar
- Os campos em `defaults` são usados apenas se for necessário criar

**URLs com Namespace vs Hardcoded**
Usar `{% url 'pharmacy:preferencias_editar' %}` em vez de `/preferencias/` garante que os links funcionam mesmo que a estrutura de URLs mude.

### Fase 9: Polimento (4 de Fevereiro de 2026)

**Localização (i18n/l10n)**
- `LANGUAGE_CODE` define o idioma da aplicação
- `TIME_ZONE` define o fuso horário
- `USE_L10N = True` activa formatação local de números e datas
- `DATE_INPUT_FORMATS` define quais formatos de data o Django aceita nos formulários

**Flatpickr**
Biblioteca JavaScript para date pickers elegantes. Integra-se adicionando a classe `datepicker` aos campos de data e inicializando com JavaScript.

**Popular Base de Dados via Django Shell**
O comando `python manage.py shell` abre um interpretador Python com acesso aos modelos Django:
```python
from pharmacy.models import Medicamento
Medicamento.objects.create(
    utilizador=user,
    nome_comercial='Ben-u-ron',
    ...
)
```
### Fase 10: Melhorias de Usabilidade Após Demo ao Professor (13 de Fevereiro de 2026)

**`__str__()` com lógica condicional**
O método `__str__()` pode incluir lógica para mostrar informação opcional:
```python
lote_info = f" - Lote: {self.lote}" if self.lote else ""
return f"{self.medicamento.nome_comercial} - Validade: {self.data_validade}{lote_info} (...)"
```

**`UserCreationForm` — formulário built-in do Django**
O Django fornece um formulário pronto para criação de utilizadores com validação de password incluída. Basta importar e usar:
```python
from django.contrib.auth.forms import UserCreationForm
```

**`messages` framework do Django**
Permite enviar mensagens entre views (ex: mostrar "Conta criada!" após redirecionar para login):
```python
from django.contrib import messages
messages.success(request, 'Conta criada com sucesso!')
```

**Views sem `@login_required`**
Páginas públicas como o registo não usam o decorador `@login_required`, caso contrário o utilizador seria redirecionado para o login antes de poder criar conta.

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

### Sessão 3 — 2 e 3 de Fevereiro de 2026
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
- **Fase 7 concluída:** Dashboard dinâmico e sistema de alertas

### Sessão 6 — 4 de Fevereiro de 2026
- **Fase 8 concluída:** Página de preferências do utilizador
  - PreferenciasForm com get_or_create()
  - Correcção do link na navbar (URL hardcoded → {% url %})
- **Fase 9 iniciada:** Polimento final
  - Utilizador Professor criado (password: DemoADS2026)
  - 10 medicamentos comuns pré-populados via Django Shell
  - README.md actualizado com instruções completas
  - Configuração de localização portuguesa (pt-pt)
  - Resolução do problema de formato de datas (dd/mm/aaaa)
  - Integração do Flatpickr para date picker com calendário

### Sessão 7 — 13 de Fevereiro de 2026
- Apresentação do projecto ao professor Alexandre Sousa
- Password do utilizador `miguel` redefinida
- Utilizador `Professor` confirmado com password `DemoADS2026`
- **Fase 10 concluída:** Melhorias de usabilidade
  - Tarefa 10.1: Lote adicionado ao dropdown de embalagens no registo de consumos (alteração do `__str__` em Embalagem)
  - Tarefa 10.2: Página de registo de novo utilizador com `UserCreationForm`
  - Mensagens de sucesso no login com `messages` framework
  - Link "Criar conta" adicionado à página de login

---

## PRÓXIMOS PASSOS

### Aplicação: ✅ COMPLETA
Todas as funcionalidades do MVP foram implementadas (Fases 0-10).

### Chat Seguinte: Documentação para Entrega
- [ ] Criar **Manual de Utilizador** (requisito obrigatório do enunciado)
  - Documento a descrever como a aplicação pode ser usada
  - Instruções passo-a-passo para cada funcionalidade
- [ ] Criar/actualizar **Relatório de Arquitectura** (requisito obrigatório do enunciado)
  - Actualizar o Guião original com as funcionalidades implementadas
  - Incluir decisões técnicas finais
- [ ] Commit final com toda a documentação
- [ ] Verificar todos os requisitos do professor (checklist completa)

---

## PROBLEMAS CONHECIDOS E SOLUÇÕES

| Problema | Solução |
|----------|---------|
| Ambiente virtual corrompido após actualização macOS | Apagar e recriar: `rm -rf venv && python3 -m venv venv` |
| Erros de favicon.ico no log | Inofensivos, browser a pedir ícone que não existe |
| Import de Preferencias errado | Importar de `.models`, não de `.forms` |
| Link da navbar dá 404 | Usar `{% url 'pharmacy:nome' %}` em vez de URLs hardcoded |
| Datas interpretadas como mm/dd/aaaa | Configurar `DATE_INPUT_FORMATS` e usar Flatpickr |

---

## CREDENCIAIS

| Ambiente | Username | Password | Notas |
|----------|----------|----------|-------|
| Django Admin (dev) | miguel | (definida pelo aluno) | Superuser para desenvolvimento |
| Django Admin (demo) | Professor | DemoADS2026 | Para demonstração ao professor |

---

## LINKS ÚTEIS

- **Repositório GitHub:** https://github.com/miguelascensaoreal/DomusShelf
- **Django Documentation:** https://docs.djangoproject.com/
- **Django Girls Tutorial (PT):** https://tutorial.djangogirls.org/pt/
- **Bootstrap 5 Docs:** https://getbootstrap.com/docs/5.3/
- **Bootstrap Icons:** https://icons.getbootstrap.com/
- **Flatpickr Docs:** https://flatpickr.js.org/

---

## NOTAS IMPORTANTES

### Estilo de Documentos
- Português de Portugal
- Todos os documentos para entrega devem ter disclaimer sobre uso de IA

### Commits
- Fazer commits frequentes com mensagens descritivas em português
- Exemplo: "Adiciona Flatpickr para date picker em formato português (dd/mm/aaaa)"

---

*Este ficheiro deve ser anexado ao início de cada novo chat para manter o contexto do projecto.*
