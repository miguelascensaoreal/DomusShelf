# 💊 DomusShelf - Sistema de Gestão de Farmácia Doméstica

Aplicação web desenvolvida em Django para gestão de medicamentos domésticos, com controlo de stock, validades e alertas automáticos.

**Autor:** Miguel Ângelo Ascensão Real  
**Número:** 48891  
**Disciplina:** Arquitectura e Desenho de Software  
**Instituição:** Universidade da Maia (UMAIA)  
**Data:** 15 de Fevereiro de 2026

---

## Objectivo

A acumulação de medicamentos com diferentes datas de validade leva frequentemente ao desperdício e, em casos graves, ao consumo de medicamentos fora de prazo. O DomusShelf resolve este problema permitindo:

- Manter um catálogo organizado de medicamentos
- Controlar o stock por embalagem com datas de validade
- Receber alertas sobre medicamentos prestes a expirar
- Registar consumos que actualizam automaticamente o stock

---

## Tecnologias Utilizadas

| Componente | Tecnologia |
|------------|------------|
| Backend | Python 3.12 + Django 4.2 |
| Base de Dados | SQLite |
| Frontend | Bootstrap 5 + Bootstrap Icons |
| Fonte | Inter (Google Fonts) |

---

## Instalação e Execução

### Pré-requisitos

- Python 3.10 ou superior
- pip (gestor de pacotes Python)
- Git

### Passos de Instalação

1. **Clonar o repositório**
```bash
   git clone https://github.com/miguelascensaoreal/DomusShelf.git
   cd DomusShelf
```

2. **Criar ambiente virtual**
```bash
   python3 -m venv venv
```

3. **Activar ambiente virtual**
   
   No macOS/Linux:
```bash
   source venv/bin/activate
```
   
   No Windows:
```bash
   venv\Scripts\activate
```

4. **Instalar dependências**
```bash
   pip install -r requirements.txt
```

5. **Aplicar migrações** (criar/actualizar base de dados)
```bash
   python manage.py migrate
```

6. **Iniciar o servidor**
```bash
   python manage.py runserver
```

7. **Aceder à aplicação**
   
   Abrir no browser: http://127.0.0.1:8000/

---

## Credenciais de Demonstração

Para facilitar a avaliação, existe um utilizador pré-configurado:

| Utilizador | Password | Tipo |
|------------|----------|------|
| Professor | DemoADS2026 | Superuser |

Este utilizador tem acesso ao painel de administração em http://127.0.0.1:8000/admin/

---

## Funcionalidades

### Gestão de Medicamentos
Catálogo pessoal de medicamentos com nome comercial, princípio activo e forma farmacêutica.

### Gestão de Stock (Embalagens)
Registo de embalagens físicas com quantidade, unidade, data de validade e lote. Ordenação automática FEFO (First Expired, First Out).

### Registo de Consumos
Registo de tomas com desconto automático do stock. Validação para impedir consumir mais do que o disponível.

### Sistema de Alertas
Notificação visual (sino com badge) de medicamentos expirados ou a expirar. Número de dias configurável nas preferências.

### Dashboard
Visão geral com estatísticas do estado da farmácia e acções rápidas.

### Multi-utilizador
Cada utilizador vê apenas os seus próprios medicamentos e stock.

---

## Estrutura do Projecto
```
DomusShelf/
├── domusshelf_project/     # Configuração central Django
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── pharmacy/               # Aplicação principal
│   ├── models.py           # Modelos de dados
│   ├── views.py            # Lógica das páginas
│   ├── forms.py            # Formulários
│   ├── urls.py             # Rotas da aplicação
│   ├── context_processors.py
│   └── templates/pharmacy/ # Templates específicos
├── templates/              # Templates globais
│   ├── base.html
│   └── registration/
├── docs/                   # Documentação
├── db.sqlite3              # Base de dados
├── requirements.txt        # Dependências Python
└── manage.py
```

---

## Modelo de Dados

O sistema utiliza quatro entidades principais:

- **Medicamento** — Catálogo de medicamentos (1 utilizador → N medicamentos)
- **Embalagem** — Stock físico com validade (1 medicamento → N embalagens)
- **Consumo** — Registo de tomas (1 embalagem → N consumos)
- **Preferências** — Configurações por utilizador (1 utilizador → 1 preferências)

---

## Licença

Projecto desenvolvido no âmbito académico da disciplina de Arquitectura e Desenho de Software do Mestrado em Informática da Universidade da Maia.

