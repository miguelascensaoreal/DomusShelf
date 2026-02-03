# DomusShelf — Registo de Desenvolvimento

**Projecto:** Sistema de Gestão de Farmácia Doméstica  
**Aluno:** Miguel Ângelo Ascensão Real (nº 48891)  
**Disciplina:** Arquitectura e Desenho de Software  
**Universidade:** UMAIA — Universidade da Maia  
**Iniciado em:** 18 de Janeiro de 2026

Este documento regista cronologicamente o desenvolvimento do projecto DomusShelf, incluindo as decisões técnicas tomadas, os problemas encontrados e as soluções aplicadas. Serve como base para o relatório académico final e como contexto para sessões de desenvolvimento futuras.

---

## Sessão 1 — 18 de Janeiro de 2026

### Objectivo da Sessão
Configuração inicial do ambiente de desenvolvimento e criação da estrutura base do projecto Django.

### Trabalho Realizado

**Configuração do ambiente de desenvolvimento.** Foi instalado e configurado o Python 3.12 no MacBook Air M3 do aluno. Optou-se por utilizar um ambiente virtual Python (venv) para isolar as dependências do projecto, seguindo as boas práticas de desenvolvimento Python. O Django 4.2.27 (versão LTS) foi instalado dentro deste ambiente virtual.

**Criação do projecto Django.** Foi criada a estrutura base do projecto usando o comando `django-admin startproject`, resultando na pasta `domusshelf_project` que contém as configurações centrais. Foi também criada a aplicação `pharmacy` usando `python manage.py startapp`, que irá conter toda a lógica de negócio da aplicação.

**Configuração do controlo de versões.** O Git foi configurado localmente e foi criado um repositório privado no GitHub. O professor foi convidado como colaborador para poder acompanhar o desenvolvimento. Foram feitos os primeiros commits com a estrutura inicial do projecto.

**Teste do ambiente.** O servidor de desenvolvimento foi iniciado com sucesso, confirmando que toda a configuração estava correcta através da visualização da página padrão do Django (foguete verde).

### Decisões Técnicas

A escolha do Django 4.2 LTS deveu-se à sua estabilidade e suporte prolongado, sendo adequado para um projecto académico. A opção pelo SQLite como base de dados justifica-se pela simplicidade de configuração (não requer servidor separado) e pela portabilidade (toda a base de dados fica num único ficheiro), facilitando a demonstração ao professor.

### Problemas Identificados

Durante o commit inicial, a pasta `venv/` foi inadvertidamente incluída no repositório, o que é uma má prática pois o ambiente virtual é específico de cada máquina e não deve ser partilhado.

---

## Sessão 2 — 2 de Fevereiro de 2026

### Objectivo da Sessão
Revisão do estado do projecto, consolidação do planeamento e criação de documentação de contexto.

### Trabalho Realizado

**Revisão das decisões técnicas.** Foram confirmadas e documentadas todas as decisões técnicas aprovadas pelo professor, incluindo a utilização de Bootstrap via CDN para o frontend e a implementação de sistema multi-utilizador usando o sistema de autenticação nativo do Django.

**Criação do ficheiro de contexto.** Foi criado o documento CONTEXTO_DOMUSSHELF.md com toda a informação necessária para retomar o desenvolvimento em sessões futuras, incluindo o modelo de dados planeado, as funcionalidades do MVP, e o plano de implementação faseado.

**Planeamento detalhado.** O desenvolvimento foi organizado em nove fases, desde a limpeza do repositório até ao polimento final, permitindo uma abordagem incremental e validação progressiva do trabalho.

---

## Sessão 3 — 3 de Fevereiro de 2026

### Objectivo da Sessão
Limpeza do repositório Git e implementação dos modelos de dados.

### Fase 0: Limpeza do Repositório

**Problema encontrado.** Ao executar `git status`, foram detectadas mais de 4200 alterações pendentes, todas relacionadas com a pasta `venv/` que estava a ser rastreada pelo Git. Isto aconteceu porque o ambiente virtual foi recriado com Python 3.12, enquanto o repositório continha ficheiros de Python 3.9.

**Solução aplicada.** O processo de limpeza envolveu três passos. Primeiro, as alterações locais foram descartadas usando `git checkout -- .` para repor os ficheiros ao estado do último commit. Depois, foi criado um ficheiro `.gitignore` com regras para ignorar permanentemente a pasta `venv/`, os ficheiros `__pycache__/`, os ficheiros `.DS_Store` do macOS, e outras pastas de configuração de editores. Finalmente, os ficheiros problemáticos foram removidos do rastreamento do Git (mas não do disco local) usando `git rm -r --cached venv/` e `git rm --cached .DS_Store`.

**Resultado.** O repositório no GitHub ficou limpo, contendo apenas os ficheiros relevantes do projecto. O ambiente virtual continua a existir localmente e a funcionar normalmente, mas deixou de ser enviado para o GitHub. Esta correcção evitará problemas semelhantes no futuro.

**Commit realizado:** "Remove venv e .DS_Store do repositório, adiciona .gitignore"

### Fase 1: Modelos de Dados

**Conceito implementado.** Os modelos em Django representam a estrutura dos dados que a aplicação vai gerir. Cada modelo corresponde a uma tabela na base de dados, e cada atributo do modelo corresponde a uma coluna dessa tabela. O Django utiliza um ORM (Object-Relational Mapping) que permite trabalhar com os dados usando código Python, sem necessidade de escrever SQL directamente.

**Modelos criados:**

O modelo **Medicamento** representa o catálogo de medicamentos conhecidos pelo utilizador. Contém os campos nome_comercial (nome que aparece na embalagem), principio_activo (substância activa), forma_farmaceutica (comprimidos, xarope, etc.), e observacoes (campo opcional para notas). Cada medicamento está associado a um utilizador específico através de uma chave estrangeira (ForeignKey) para o modelo User do Django.

O modelo **Embalagem** representa uma unidade física de stock, ou seja, uma caixa ou frasco concreto. Está associado a um medicamento através de ForeignKey, permitindo que o mesmo medicamento tenha múltiplas embalagens com validades diferentes. Os campos incluem quantidade_inicial (o que vinha na embalagem), quantidade_actual (o que resta), unidade (comprimidos, ml, etc.), data_validade, e lote (opcional). A relação com Medicamento usa `on_delete=models.CASCADE`, significando que se um medicamento for eliminado, todas as suas embalagens são também eliminadas automaticamente.

O modelo **Consumo** regista cada utilização de medicamento. Está associado a uma embalagem específica e contém a quantidade consumida, a data e hora do consumo, e observações opcionais. Este modelo permite rastrear o histórico de tomas e serve de base para o cálculo automático da quantidade restante em cada embalagem.

O modelo **Preferencias** armazena as configurações pessoais de cada utilizador. Utiliza uma relação OneToOneField com o modelo User, garantindo que cada utilizador tem exactamente um registo de preferências. O campo principal é dias_alerta_antes, que define com quantos dias de antecedência o utilizador quer ser alertado sobre medicamentos prestes a expirar.

**Métodos auxiliares implementados:**

Cada modelo inclui um método `__str__` que define como o objecto é representado em texto, facilitando a identificação no Django Admin e na depuração.

O modelo Embalagem inclui uma propriedade `esta_expirada` que verifica se a data de validade já passou, e uma propriedade `dias_para_expirar` que calcula quantos dias faltam para a validade. Estas propriedades são usadas pelo sistema de alertas.

O modelo Embalagem define também uma ordenação padrão através da classe Meta com `ordering = ['data_validade']`, implementando automaticamente o princípio FEFO (First Expired, First Out) — as embalagens com validade mais próxima aparecem primeiro nas listagens.

**Migrações.** Após definir os modelos, foi executado `python manage.py makemigrations` para gerar o ficheiro de migração, e `python manage.py migrate` para aplicar as alterações à base de dados. Este processo criou as tabelas necessárias no ficheiro SQLite.

**Registo no Django Admin.** Os modelos foram registados no ficheiro `admin.py` com configurações personalizadas (classes ModelAdmin) que definem quais campos aparecem na listagem, quais são pesquisáveis, e como os dados são filtrados. Isto permite gerir os dados através do painel de administração do Django sem necessidade de criar interfaces específicas.

**Teste realizado.** Foi criado um superutilizador para aceder ao Django Admin. Através do painel, foram inseridos dados de teste (medicamentos e embalagens) para verificar que os modelos funcionam correctamente e que as relações entre eles estão bem definidas.

**Commit realizado:** "Implementa modelos de dados: Medicamento, Embalagem, Consumo, Preferencias"

---

## Conceitos Técnicos para o Relatório

### Padrão MTV (Model-Template-View)

O Django utiliza uma variante do padrão arquitectural MVC (Model-View-Controller) denominada MTV. O **Model** representa os dados e a lógica de negócio, definindo a estrutura da informação e as regras de validação. O **Template** é responsável pela apresentação, definindo como a informação é mostrada ao utilizador através de HTML com marcadores especiais do Django. A **View** actua como controlador, processando os pedidos HTTP, interagindo com os modelos para obter ou modificar dados, e seleccionando o template apropriado para a resposta.

### ORM (Object-Relational Mapping)

O ORM do Django permite trabalhar com bases de dados usando código Python em vez de SQL. Cada classe que herda de `models.Model` corresponde a uma tabela na base de dados. Os atributos da classe (como `CharField`, `IntegerField`, `DateField`) correspondem a colunas com os respectivos tipos de dados. As relações entre tabelas são definidas através de campos especiais como `ForeignKey` (um para muitos) e `OneToOneField` (um para um). O Django traduz automaticamente as operações Python em queries SQL, abstraindo a complexidade da base de dados.

### Migrações

O sistema de migrações do Django permite evoluir a estrutura da base de dados de forma controlada. Quando os modelos são alterados, o comando `makemigrations` detecta as diferenças e gera ficheiros de migração que descrevem as alterações necessárias. O comando `migrate` aplica essas alterações à base de dados. Este sistema mantém um histórico de todas as alterações estruturais e permite que a base de dados seja recriada do zero ou actualizada incrementalmente.

---

## Próximos Passos

A próxima fase (Fase 2) consistirá na configuração do sistema de autenticação, incluindo as páginas de login e logout. Seguir-se-á a criação do template base com Bootstrap e a implementação das operações CRUD para medicamentos e embalagens.

---

*Nota: Foi utilizada uma LLM (Claude AI) como ferramenta de apoio no desenvolvimento e documentação deste projecto, não para realização de trabalho completo.*
