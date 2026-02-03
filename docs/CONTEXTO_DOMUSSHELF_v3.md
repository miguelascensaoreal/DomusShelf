# DomusShelf - Ficheiro de Contexto para Continuação do Projecto

**Data de criação deste documento:** 2 de Fevereiro de 2026  
**Última actualização:** 3 de Fevereiro de 2026 (após Fase 2)  
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
4. ✅ Funcionar minimamente (modelos, admin e autenticação funcionais)
5. ✅ Armazenar dados em base de dados (SQLite com tabelas criadas)
6. ✅ Código fonte em controlo de versões (Git)
7. ✅ Código fonte no GitHub (repositório privado com 5 commits)
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
| Tema Visual | Fundo branco, acentos vermelho escuro (#8B0000) | Preferência do aluno |
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
- Configuração de `LOGIN_REDIRECT_URL` e `LOGOUT_REDIRECT_URL`
- Login e logout testados e funcionais

### Estrutura Actual do Projecto

```
DomusShelf/
├── docs/                       # Documentação do projecto
│   ├── ARRANCAR_PROJECTO.md
│   ├── CONTEXTO_DOMUSSHELF_v2.md
│   └── REGISTO_DESENVOLVIMENTO.md
├── domusshelf_project/         # Configuração central Django
│   ├── __init__.py
│   ├── settings.py             # ✅ TEMPLATES e redirects configurados
│   ├── urls.py                 # ✅ URLs de autenticação adicionadas
│   ├── asgi.py
│   └── wsgi.py
├── pharmacy/                   # App principal
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py     # ✅ Migração dos modelos
│   ├── __init__.py
│   ├── admin.py                # ✅ Configuração do Admin
│   ├── apps.py
│   ├── models.py               # ✅ 4 modelos implementados
│   ├── tests.py
│   └── views.py                # VAZIO - próxima fase
├── templates/                  # ✅ Templates globais
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
- **Commits:** 5 commits realizados
- **Último commit:** "Implementa sistema de autenticação com página de login personalizada"

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
| F5 | Dashboard | Visão geral + acções rápidas | ⬜ Pendente |
| F6 | Preferências | Configurar dias de alerta | ⬜ Pendente |
| F7 | Autenticação | Login/Logout (Django built-in) | ✅ Concluído |
| F8 | Registo de Utilizador | Criar conta nova | ⬜ Opcional |

**Nota:** Os modelos de dados (base de F1-F6) estão implementados. Falta criar as Views e Templates.

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
- [x] Configurar LOGIN_REDIRECT_URL e LOGOUT_REDIRECT_URL
- [x] Testar login e logout
- [x] Commit e push

### Fase 3: Template Base e Navegação ⬜ PRÓXIMA
**Tempo estimado:** 45 minutos
- [ ] Criar `templates/base.html` com Bootstrap CDN
- [ ] Implementar navbar responsiva
- [ ] Adicionar ícone de alertas (sino) com badge
- [ ] Aplicar tema visual (vermelho escuro, fonte personalizada)
- [ ] Actualizar login.html para herdar do base.html
- [ ] Testar responsividade (mobile)
- [ ] Commit e push

### Fase 4: CRUD Medicamentos ⬜
**Tempo estimado:** 1-2 horas
- [ ] View: lista de medicamentos (filtrada por utilizador)
- [ ] View: criar medicamento
- [ ] View: editar medicamento
- [ ] View: eliminar medicamento (com confirmação)
- [ ] Templates correspondentes
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
- [ ] View: dashboard com estatísticas
- [ ] Lógica de cálculo de alertas (expirados + a expirar)
- [ ] Badge dinâmico no sino (context processor ou middleware)
- [ ] Página dedicada de alertas
- [ ] Acções rápidas no dashboard
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
| `/admin/` | Painel de administração Django | ✅ Funcional |
| `/accounts/login/` | Página de login | ✅ Funcional |
| `/accounts/logout/` | Logout (redireciona para login) | ✅ Funcional |
| `/` | Página inicial (redireciona para admin temporariamente) | ✅ Funcional |

## URLs A IMPLEMENTAR (Fases seguintes)

| URL | Função | Fase |
|-----|--------|------|
| `/` | Dashboard (substituirá o redirect actual) | Fase 7 |
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
- Configuração do VS Code para usar o Python do venv
- 5 commits no GitHub

---

## PRÓXIMA SESSÃO

**Começar por:** Fase 3 (Template Base e Navegação)

**Primeiro comando a executar:**
```bash
cd ~/Documents/DomusShelf
source venv/bin/activate
python manage.py runserver
```

**Verificar que funciona:** Aceder a http://127.0.0.1:8000/accounts/login/ e ver a página de login

**Tarefas da Fase 3:**
- Criar template base (`templates/base.html`)
- Implementar navbar responsiva com Bootstrap 5
- Adicionar ícone de sino para alertas
- Definir fonte e esquema de cores final
- Actualizar login.html para usar o template base

---

## NOTAS IMPORTANTES

### Estilo de Documentos
- Português de Portugal sem novo acordo ortográfico
- Todos os documentos para entrega devem ter disclaimer sobre uso de IA
- Formato do disclaimer: "Foi utilizada uma LLM (Claude AI) como ferramenta de apoio, não para realização de trabalho completo."

### Commits
- Fazer commits frequentes com mensagens descritivas em português
- Exemplo: "Adiciona modelo Medicamento com campos base"

### Testes
- Testar sempre em modo mobile (F12 no browser → toggle device toolbar)
- Verificar que cada funcionalidade filtra por utilizador autenticado

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

---

*Este ficheiro deve ser anexado ao início de cada novo chat para manter o contexto do projecto.*
