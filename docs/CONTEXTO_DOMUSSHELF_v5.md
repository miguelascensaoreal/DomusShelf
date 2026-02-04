# DomusShelf - Ficheiro de Contexto para Continuação do Projecto

**Data de criação deste documento:** 2 de Fevereiro de 2026  
**Última actualização:** 3 de Fevereiro de 2026 (após Fase 5)  
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
4. ✅ Funcionar minimamente (CRUD medicamentos e embalagens funcionais)
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
- Dados de teste inseridos (Ben-u-ron 1g com uma embalagem)

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
  - Sino de alertas preparado para badge dinâmico
  - Dropdown de utilizador com Preferências, Administração e Sair
  - Footer com copyright
  - Blocos para herança de templates (title, content, extra_css, extra_js)
- Dashboard inicial criado (`pharmacy/templates/pharmacy/dashboard.html`)
  - Herda do base.html usando `{% extends 'base.html' %}`
  - Cards de acesso rápido para todas as funcionalidades
  - Design responsivo testado em modo mobile
- View `dashboard` criada em `pharmacy/views.py` com decorador `@login_required`
- URLs actualizadas para página inicial apontar para o dashboard
- Responsividade testada (Safari Responsive Design Mode)

**Fase 4: CRUD Medicamentos** ✅ (3 de Fevereiro de 2026)
- Ficheiro `pharmacy/urls.py` criado com namespace `pharmacy`
- Ficheiro `pharmacy/forms.py` criado com `MedicamentoForm` (ModelForm)
- Quatro views implementadas em `pharmacy/views.py`:
  - `medicamento_lista` — lista filtrada por utilizador
  - `medicamento_criar` — formulário com `commit=False` para associar utilizador
  - `medicamento_editar` — formulário com `instance` para edição
  - `medicamento_eliminar` — confirmação POST antes de apagar
- Três templates criados:
  - `medicamento_lista.html` — tabela desktop + cards mobile
  - `medicamento_form.html` — reutilizado para criar e editar
  - `medicamento_confirmar_eliminar.html` — página de confirmação
- URLs ligadas ao `domusshelf_project/urls.py` com `include()`
- Segurança: filtro por `utilizador=request.user` em todas as views
- Testado: criar, editar, listar e eliminar medicamentos

**Fase 5: CRUD Embalagens** ✅ (3 de Fevereiro de 2026)
- URLs de embalagens adicionadas a `pharmacy/urls.py` (prefixo `stock/`)
- `EmbalagemForm` criado em `pharmacy/forms.py` com:
  - Dropdown de medicamentos filtrado por utilizador (`__init__` personalizado)
  - Widget de data (`type: date`) para data de validade
  - Campos quantidade e unidade lado a lado no formulário
- Quatro views implementadas:
  - `embalagem_lista` — ordenada por `data_validade` (FEFO), usa `select_related`
  - `embalagem_criar` — define `quantidade_actual = quantidade_inicial`
  - `embalagem_editar` — com filtro `medicamento__utilizador`
  - `embalagem_eliminar` — confirmação com detalhes da embalagem
- Três templates criados:
  - `embalagem_lista.html` — com indicadores visuais de validade (badges coloridos)
  - `embalagem_form.html` — com link para criar medicamento
  - `embalagem_confirmar_eliminar.html` — mostra detalhes antes de apagar
- Indicadores visuais: vermelho (expirado), amarelo (≤30 dias), verde (OK)
- Links da navbar actualizados para usar `{% url %}`

### Estrutura Actual do Projecto

```
DomusShelf/
├── docs/                       # Documentação do projecto
│   ├── ARRANCAR_PROJECTO.md
│   ├── CONTEXTO_DOMUSSHELF.md
│   └── REGISTO_DESENVOLVIMENTO.md
├── domusshelf_project/         # Configuração central Django
│   ├── __init__.py
│   ├── settings.py             # ✅ TEMPLATES, LOGIN_URL configurados
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
│   │   └── embalagem_confirmar_eliminar.html
│   ├── __init__.py
│   ├── admin.py                # ✅ Configuração do Admin
│   ├── apps.py
│   ├── forms.py                # ✅ MedicamentoForm + EmbalagemForm
│   ├── models.py               # ✅ 4 modelos implementados
│   ├── tests.py
│   ├── urls.py                 # ✅ URLs da app com namespace
│   └── views.py                # ✅ Dashboard + CRUD medicamentos + CRUD embalagens
├── templates/                  # ✅ Templates globais
│   ├── base.html               # ✅ Template base com navbar
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
- **Commits realizados** (lista a actualizar após push)
- **Último commit esperado:** "Implementa CRUD completo de embalagens (Fase 5)"

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
- Brufen: 20 comprimidos, validade 20/02/2026, lote ABC321 (a expirar em breve)

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

---

## FUNCIONALIDADES DO MVP

| ID | Funcionalidade | Descrição | Estado |
|----|----------------|-----------|--------|
| F1 | Gestão de Medicamentos | CRUD completo do catálogo | ✅ Concluído |
| F2 | Gestão de Embalagens | CRUD com ordenação FEFO | ✅ Concluído |
| F3 | Registo de Consumos | Formulário + desconto automático | ⬜ Pendente |
| F4 | Sistema de Alertas | Sino com badge + página de alertas | ⬜ Pendente |
| F5 | Dashboard | Visão geral + acções rápidas | ✅ Estrutura criada |
| F6 | Preferências | Configurar dias de alerta | ⬜ Pendente |
| F7 | Autenticação | Login/Logout (Django built-in) | ✅ Concluído |
| F8 | Registo de Utilizador | Criar conta nova | ⬜ Opcional |

---

## PLANO DE IMPLEMENTAÇÃO (Fases)

### Fase 0: Limpeza e Preparação ✅ CONCLUÍDA

### Fase 1: Modelos de Dados ✅ CONCLUÍDA

### Fase 2: Autenticação ✅ CONCLUÍDA

### Fase 3: Template Base e Navegação ✅ CONCLUÍDA

### Fase 4: CRUD Medicamentos ✅ CONCLUÍDA
- [x] Criar ficheiro `pharmacy/urls.py` com namespace
- [x] Ligar ao `urls.py` principal com `include()`
- [x] Criar `pharmacy/forms.py` com MedicamentoForm
- [x] View: lista de medicamentos (filtrada por utilizador)
- [x] View: criar medicamento
- [x] View: editar medicamento
- [x] View: eliminar medicamento (com confirmação)
- [x] Templates correspondentes (lista, form, confirmar)
- [x] Commit e push

### Fase 5: CRUD Embalagens ✅ CONCLUÍDA
- [x] URLs de embalagens em `pharmacy/urls.py`
- [x] EmbalagemForm com dropdown filtrado por utilizador
- [x] View: lista de embalagens (ordenada por validade - FEFO)
- [x] View: criar embalagem (quantidade_actual = quantidade_inicial)
- [x] View: editar embalagem
- [x] View: eliminar embalagem
- [x] Templates com indicadores visuais de validade
- [x] Commit e push

### Fase 6: Registo de Consumos ⬜ PRÓXIMA
**Tempo estimado:** 1 hora
- [ ] Criar ConsumoForm em `pharmacy/forms.py`
- [ ] View: formulário de consumo (`consumo_criar`)
- [ ] Lógica de desconto automático (`quantidade_actual -= quantidade`)
- [ ] Validação (não permitir consumo > quantidade disponível)
- [ ] Template do formulário
- [ ] Actualizar link "Registar Toma" na navbar
- [ ] Commit e push

### Fase 7: Dashboard e Alertas ⬜
**Tempo estimado:** 1-2 horas
- [ ] Melhorar dashboard com estatísticas reais
- [ ] Lógica de cálculo de alertas (expirados + a expirar)
- [ ] Badge dinâmico no sino (context processor)
- [ ] Página dedicada de alertas
- [ ] Commit e push

### Fase 8: Preferências ⬜
**Tempo estimado:** 30 minutos
- [ ] View: página de preferências
- [ ] Formulário para dias_alerta_antes
- [ ] Criar Preferencias automaticamente para novos utilizadores
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

## URLs A IMPLEMENTAR (Fases seguintes)

| URL | Função | Fase |
|-----|--------|------|
| `/consumos/novo/` | Formulário de toma | Fase 6 |
| `/alertas/` | Lista expirados + a expirar | Fase 7 |
| `/preferencias/` | Configuração | Fase 8 |

---

## CONCEITOS DJANGO APRENDIDOS

### Herança de Templates
O ficheiro `base.html` define a estrutura comum (navbar, estilos, footer) usando blocos como `{% block content %}{% endblock %}`. Os templates filhos usam `{% extends 'base.html' %}` e preenchem apenas os blocos que precisam alterar. Isto evita repetição de código.

### Decorador @login_required
Colocado antes de uma view, garante que apenas utilizadores autenticados podem aceder. Se não estiver autenticado, o Django redireciona automaticamente para `LOGIN_URL`.

### Variável {{ user }}
O Django disponibiliza automaticamente o objecto `user` em todos os templates. Podemos usar `user.username`, `user.is_authenticated`, etc.

### Responsividade Bootstrap
A classe `navbar-expand-lg` faz a navbar colapsar em ecrãs menores que "large". O sistema de grid (`col-md-6 col-lg-4`) faz os cards reorganizarem-se conforme o tamanho do ecrã.

### URLs com Namespaces (Fase 4)
O `app_name = 'pharmacy'` no `urls.py` da app cria um namespace. Nos templates, usamos `{% url 'pharmacy:medicamento_lista' %}` para evitar conflitos de nomes entre apps diferentes.

### Path Converters (Fase 4)
A sintaxe `<int:pk>` nas URLs captura um número inteiro e passa-o à view como argumento. Ex: `/medicamentos/5/editar/` passa `pk=5` à view `medicamento_editar`.

### ModelForms (Fase 4)
A classe `MedicamentoForm(forms.ModelForm)` gera automaticamente um formulário a partir do modelo. A classe `Meta` define qual modelo usar e quais campos incluir.

### Padrão GET/POST nas Views (Fase 4)
Uma mesma view pode tratar pedidos GET (mostrar formulário vazio) e POST (processar dados submetidos). Usamos `if request.method == 'POST'` para distinguir.

### commit=False (Fase 4)
Ao fazer `form.save(commit=False)`, o Django cria o objecto em memória mas não guarda na BD. Isto permite modificar campos (como associar o utilizador) antes de guardar com `save()`.

### get_object_or_404 (Fase 4)
Esta função busca um objecto na BD ou devolve erro 404 automaticamente. Mais seguro e limpo que try/except manual.

### Filtrar por Relação com __ (Fase 5)
O duplo underscore permite atravessar relações ForeignKey. Ex: `medicamento__utilizador=request.user` filtra embalagens cujo medicamento pertence ao utilizador.

### select_related (Fase 5)
Optimização que carrega dados relacionados na mesma query SQL (JOIN). Evita o problema "N+1 queries" quando acedemos a `embalagem.medicamento` no template.

### __init__ Personalizado em Forms (Fase 5)
Sobrescrever o método `__init__` permite receber parâmetros extra (como `user`) e modificar o formulário dinamicamente (ex: filtrar o queryset de um dropdown).

### kwargs.pop() (Fase 5)
Remove e devolve um valor do dicionário de argumentos. Necessário porque a classe pai (ModelForm) não espera argumentos personalizados como `user`.

### Widget de Data (Fase 5)
Usar `'type': 'date'` no widget faz o browser mostrar um date picker nativo, melhorando a usabilidade.

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
- **Fase 0 concluída:** Limpeza do repositório (removido venv/ e .DS_Store, criado .gitignore)
- **Fase 1 concluída:** Implementação dos 4 modelos de dados, configuração do Django Admin
- **Fase 2 concluída:** Sistema de autenticação com página de login personalizada
- **Fase 3 concluída:** Template base com navbar responsiva, dashboard inicial
- Testada responsividade em Safari Responsive Design Mode

### Sessão 4 — 3 de Fevereiro de 2026
- **Fase 4 concluída:** CRUD completo de medicamentos
  - Criado `pharmacy/urls.py` com namespace
  - Criado `pharmacy/forms.py` com MedicamentoForm
  - Implementadas 4 views (listar, criar, editar, eliminar)
  - Criados 3 templates (lista, formulário, confirmação)
  - Segurança: filtro por utilizador em todas as operações
- **Fase 5 concluída:** CRUD completo de embalagens
  - EmbalagemForm com dropdown filtrado por utilizador
  - Lista ordenada por validade (FEFO)
  - Indicadores visuais: vermelho (expirado), amarelo (≤30 dias), verde (OK)
  - Optimização com select_related

---

## PRÓXIMA SESSÃO

**Começar por:** Fase 6 (Registo de Consumos)

**Primeiro comando a executar:**
```bash
cd ~/Documents/DomusShelf
source venv/bin/activate
python manage.py runserver
```

**Verificar que funciona:** Aceder a http://127.0.0.1:8000/ e navegar para Stock

**Tarefas da Fase 6:**
- Criar ConsumoForm em `pharmacy/forms.py`
- Criar view `consumo_criar` para registar tomas
- Implementar lógica de desconto automático (quantidade_actual -= quantidade)
- Validar que consumo não excede quantidade disponível
- Criar template do formulário
- Actualizar link "Registar Toma" na navbar

**Conceitos novos esperados:**
- Validação personalizada em forms (método `clean()`)
- Actualizar objecto relacionado (decrementar stock da embalagem)
- Transacções atómicas (opcional, para garantir integridade)

---

## NOTAS IMPORTANTES

### Estilo de Documentos
- Português de Portugal sem novo acordo ortográfico
- Todos os documentos para entrega devem ter disclaimer sobre uso de IA
- Formato do disclaimer: "Foi utilizada uma LLM (Claude AI) como ferramenta de apoio, não para realização de trabalho completo."

### Commits
- Fazer commits frequentes com mensagens descritivas em português
- Exemplo: "Implementa CRUD completo de medicamentos (Fase 4)"

### Testes de Responsividade
- Safari: Activar Develop menu em Settings → Advanced → Show Develop menu
- Usar Develop → Enter Responsive Design Mode
- Ou simplesmente redimensionar a janela do browser

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
