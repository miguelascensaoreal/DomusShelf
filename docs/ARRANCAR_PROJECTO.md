# DomusShelf — Guia de Arranque do Projecto

**Autor:** Miguel Ângelo Ascensão Real  
**Última actualização:** 3 de Fevereiro de 2026

Este documento descreve os passos necessários para arrancar o ambiente de desenvolvimento do DomusShelf sempre que reiniciares o Mac ou começares uma nova sessão de trabalho.

---

## Arrancar o Projecto

Sempre que quiseres trabalhar no DomusShelf, segue estes quatro passos pela ordem indicada.

**Passo 1 — Abrir o Terminal**

Pressiona `Command + Space` para abrir o Spotlight, escreve "Terminal" e carrega Enter.

**Passo 2 — Navegar para a pasta do projecto**

```bash
cd ~/Documents/DomusShelf
```

**Passo 3 — Activar o ambiente virtual**

```bash
source venv/bin/activate
```

Após este comando, deverás ver `(venv)` no início da linha do terminal. Isto confirma que o ambiente virtual está activo e que o Python vai usar as bibliotecas correctas (Django, etc.).

**Passo 4 — Arrancar o servidor Django**

```bash
python manage.py runserver
```

Deverás ver uma mensagem semelhante a esta:

```
Starting development server at http://127.0.0.1:8000/
```

**Passo 5 — Aceder à aplicação**

Abre o navegador e vai a: http://127.0.0.1:8000/

---

## Parar o Servidor

No Terminal onde o servidor está em execução, pressiona:

```
Control + C
```

O servidor pára e podes fechar o Terminal ou continuar a trabalhar.

---

## Comandos Git para o Desenvolvimento

Durante o desenvolvimento, deves guardar regularmente o teu trabalho no GitHub. Isto cria um histórico das alterações e protege-te contra perda de dados.

### Ver o estado actual

Antes de fazeres commit, verifica quais ficheiros foram alterados:

```bash
git status
```

Os ficheiros a vermelho são alterações que ainda não foram adicionadas. Os ficheiros a verde estão prontos para commit.

### Guardar alterações (Commit + Push)

Quando terminares uma tarefa ou funcionalidade, executa estes três comandos:

```bash
git add .
git commit -m "Descrição breve do que foi feito"
git push origin main
```

**Exemplos de boas mensagens de commit:**

```bash
git commit -m "Adiciona modelos Medicamento e Embalagem"
git commit -m "Implementa listagem de medicamentos"
git commit -m "Corrige bug no cálculo de alertas"
git commit -m "Adiciona template base com Bootstrap"
```

### Ver histórico de commits

Para ver os commits anteriores:

```bash
git log --oneline
```

Para sair da visualização do log, pressiona `q`.

### Desfazer alterações não guardadas

Se fizeste alterações que queres descartar (voltar ao último commit):

```bash
git checkout -- .
```

**Atenção:** Este comando apaga todas as alterações locais não guardadas.

---

## Comandos Django Úteis

### Criar migrações após alterar models.py

```bash
python manage.py makemigrations
```

### Aplicar migrações à base de dados

```bash
python manage.py migrate
```

### Criar um superutilizador para o Django Admin

```bash
python manage.py createsuperuser
```

Depois podes aceder ao painel de administração em: http://127.0.0.1:8000/admin/

### Abrir a shell interactiva do Django

```bash
python manage.py shell
```

Para sair da shell, escreve `exit()` ou pressiona `Control + D`.

---

## Resumo Rápido (Cola)

| Tarefa | Comando |
|--------|---------|
| Ir para o projecto | `cd ~/Documents/DomusShelf` |
| Activar venv | `source venv/bin/activate` |
| Arrancar servidor | `python manage.py runserver` |
| Parar servidor | `Control + C` |
| Ver estado git | `git status` |
| Guardar tudo | `git add . && git commit -m "msg" && git push origin main` |
| Criar migrações | `python manage.py makemigrations` |
| Aplicar migrações | `python manage.py migrate` |

---

## Resolução de Problemas

**O terminal diz "command not found: python"**

Provavelmente esqueceste-te de activar o ambiente virtual. Executa `source venv/bin/activate` primeiro.

**O servidor não arranca e mostra erro de porta ocupada**

Outro processo está a usar a porta 8000. Podes usar uma porta diferente:

```bash
python manage.py runserver 8001
```

E depois acede a http://127.0.0.1:8001/

**O git push pede username/password**

O teu token de acesso pode ter expirado. Cria um novo Personal Access Token no GitHub e usa-o como password.

---

*Nota: Foi utilizada uma LLM (Claude AI) como ferramenta de apoio na elaboração deste documento, não para realização de trabalho completo.*
