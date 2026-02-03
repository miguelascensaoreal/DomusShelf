# DomusShelf - Ficheiro de Contexto para Continuação do Projecto

**Data de criação deste documento:** 2 de Fevereiro de 2026  
**Última actualização:** 3 de Fevereiro de 2026 (após Fase 3)  
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
4. ✅ Funcionar minimamente (modelos, admin, autenticação e dashboard funcionais)
5. ✅ Armazenar dados em base de dados (SQLite com tabelas criadas)
6. ✅ Código fonte em controlo de versões (Git)
7. ✅ Código fonte no GitHub (repositório privado com 6 commits)
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
│   ├── urls.py                 # ✅ URLs de auth + dashboard
│   ├── asgi.py
│   └── wsgi.py
├── pharmacy/                   # App principal
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py     # ✅ Migração dos modelos
│   ├── templates/              # ✅ Templates específicos da app
│   │   └── pharmacy/
│   │       └── dashboard.html  # ✅ Dashboard inicial
│   ├── __init__.py
│   ├── admin.py                # ✅ Configuração do Admin
│   ├── apps.py
│   ├── models.py               # ✅ 4 modelos implementados
│   ├── tests.py
│   └── views.py                # ✅ View do dashboard
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
- **Commits:** 6 commits realizados
- **Último commit:** "Adiciona template base com navbar responsiva e dashboard inicial"

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

- 1 Medicamento: Ben-u-ron 1gr (Paracetamol), Comprimidos
- 1 Embalagem: 20 comprimidos, validade 2028-11-30, lote 619K241

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
| F1 | Gestão de Medicamentos | CRUD completo do catálogo | ⬜ Pendente |
| F2 | Gestão de Embalagens | CRUD com ordenação FEFO | ⬜ Pendente |
| F3 | Registo de Consumos | Formulário + desconto automático | ⬜ Pendente |
| F4 | Sistema de Alertas | Sino com badge + página de alertas | ⬜ Pendente |
| F5 | Dashboard | Visão geral + acções rápidas | ✅ Estrutura criada |
| F6 | Preferências | Configurar dias de alerta | ⬜ Pendente |
| F7 | Autenticação | Login/Logout (Django built-in) | ✅ Concluído |
| F8 | Registo de Utilizador | Criar conta nova | ⬜ Opcional |

---

## PLANO DE IMPLEMENTAÇÃO (Fases)

### Fase 0: Limpeza e Preparação ✅ CONCLUÍDA
- [x] Adicionar ficheiro `.gitignore`
- [x] Remover `venv/` do tracking do Git
- [x] Remover `.DS_Store` do tracking do Git
- [x] Commit e push das correcções
- [x] Verificar que o projecto ainda corre localmente

### Fase 1: Modelos de Dados ✅ CONCLUÍDA
- [x] Criar modelos em `pharmacy/models.py`
- [x] Registar modelos no Django Admin (`pharmacy/admin.py`)
- [x] Criar e aplicar migrações
- [x] Testar no Django Admin (criar dados de teste)
- [x] Commit e push

### Fase 2: Autenticação ✅ CONCLUÍDA
- [x] Configurar URLs de autenticação no `urls.py`
- [x] Criar pasta `templates/registration/`
- [x] Criar template de login com Bootstrap 5 e tema vermelho escuro
- [x] Configurar TEMPLATES em settings.py
- [x] Configurar LOGIN_URL, LOGIN_REDIRECT_URL e LOGOUT_REDIRECT_URL
- [x] Testar login e logout
- [x] Commit e push

### Fase 3: Template Base e Navegação ✅ CONCLUÍDA
- [x] Criar `templates/base.html` com Bootstrap CDN
- [x] Adicionar Bootstrap Icons e Google Fonts (Inter)
- [x] Implementar navbar responsiva com menu hamburger
- [x] Adicionar logótipo (emoji 💊)
- [x] Adicionar ícone de alertas (sino) preparado para badge
- [x] Implementar dropdown de utilizador
- [x] Aplicar tema visual (vermelho escuro #8B0000)
- [x] Criar dashboard inicial com cards de acesso rápido
- [x] Criar view dashboard com @login_required
- [x] Testar responsividade em modo mobile
- [x] Commit e push

### Fase 4: CRUD Medicamentos ⬜ PRÓXIMA
**Tempo estimado:** 1-2 horas
- [ ] View: lista de medicamentos (filtrada por utilizador)
- [ ] View: criar medicamento
- [ ] View: editar medicamento
- [ ] View: eliminar medicamento (com confirmação)
- [ ] Templates correspondentes
- [ ] URLs da app pharmacy
- [ ] Commit e push

### Fase 5: CRUD Embalagens ⬜
**Tempo estimado:** 1-2 horas
- [ ] View: lista de embalagens (ordenada por validade - FEFO)
- [ ] View: criar embalagem (associada a medicamento)
- [ ] View: editar embalagem
- [ ] View: eliminar embalagem
- [ ] Templates correspondentes
- [ ] Commit e push

### Fase 6: Registo de Consumos ⬜
**Tempo estimado:** 1 hora
- [ ] View: formulário de consumo
- [ ] Lógica de desconto automático (quantidade_actual -= quantidade)
- [ ] Validação (não permitir consumo > quantidade disponível)
- [ ] Template do formulário
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

## URLs A IMPLEMENTAR (Fases seguintes)

| URL | Função | Fase |
|-----|--------|------|
| `/medicamentos/` | Lista do catálogo | Fase 4 |
| `/medicamentos/novo/` | Formulário criação | Fase 4 |
| `/medicamentos/<id>/editar/` | Formulário edição | Fase 4 |
| `/medicamentos/<id>/eliminar/` | Confirmação eliminação | Fase 4 |
| `/embalagens/` | Lista de stock (ordenada) | Fase 5 |
| `/embalagens/nova/` | Adicionar ao stock | Fase 5 |
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
- 6 commits no GitHub

---

## PRÓXIMA SESSÃO

**Começar por:** Fase 4 (CRUD de Medicamentos)

**Primeiro comando a executar:**
```bash
cd ~/Documents/DomusShelf
source venv/bin/activate
python manage.py runserver
```

**Verificar que funciona:** Aceder a http://127.0.0.1:8000/ e ver o dashboard

**Tarefas da Fase 4:**
- Criar URLs específicas da app pharmacy (`pharmacy/urls.py`)
- Criar views para listar, criar, editar e eliminar medicamentos
- Criar templates correspondentes (lista, formulário, confirmação)
- Filtrar medicamentos por utilizador autenticado

---

## NOTAS IMPORTANTES

### Estilo de Documentos
- Português de Portugal sem novo acordo ortográfico
- Todos os documentos para entrega devem ter disclaimer sobre uso de IA
- Formato do disclaimer: "Foi utilizada uma LLM (Claude AI) como ferramenta de apoio, não para realização de trabalho completo."

### Commits
- Fazer commits frequentes com mensagens descritivas em português
- Exemplo: "Adiciona CRUD completo de medicamentos"

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
