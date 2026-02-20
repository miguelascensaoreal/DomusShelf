# 💊 DomusShelf — Gestão de Farmácia Doméstica

Aplicação web para gerir a farmácia de casa: catalogar medicamentos, controlar stock e validades, e registar consumos. Pensada para uso familiar — todos os membros da família partilham o mesmo armário de medicamentos.

## Stack Tecnológico

- Python 3.12
- Django 4.2 (LTS)
- SQLite
- Bootstrap 5

## Como Correr Localmente
```bash
git clone https://github.com/miguelascensaoreal/DomusShelf.git
cd DomusShelf
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Abrir no browser: `http://127.0.0.1:8000/`

## Estado

🚧 Em desenvolvimento activo (v2)

## Autor

Miguel Real