# DomusShelf - Sumário de Utilização de Inteligência Artificial

**Aluno:** Miguel Ângelo Ascensão Real, n.º 48891  
**Disciplina:** Arquitectura e Desenho de Software  
**Universidade:** Universidade da Maia  
**Professor:** Alexandre Sousa  
**Data:** 15 de Fevereiro de 2026

---

## 1. Sistemas de IA Utilizados

### 1.1 Ferramenta

Foi utilizado exclusivamente o **Claude AI da Anthropic**, através da interface Claude Desktop (claude.ai). Toda a interacção decorreu dentro de um **Projecto Claude** dedicado ao DomusShelf, que permitiu manter ficheiros de referência (enunciado, guião, ficheiro de contexto) acessíveis a todas as conversas.

### 1.2 Escolha Deliberada da Interface

A opção pelo Claude Desktop, em detrimento de ferramentas como o Claude Code (agente de programação automática no terminal) ou integrações directas no IDE (extensões do VS Code), foi uma decisão consciente. O objectivo não era apenas produzir código funcional, mas compreender profundamente o que estava a ser implementado.

A utilização do Claude Desktop obrigou a um fluxo de trabalho manual: cada ficheiro foi criado ou editado por mim, no VS Code, cada comando foi executado manualmente no Terminal, e cada decisão técnica foi tomada após compreensão do seu propósito. Esta abordagem é análoga à diferença entre conduzir um automóvel e ser passageiro num táxi autónomo: ambos chegam ao destino, mas apenas o condutor desenvolve competências de navegação.

O controlo e compreensão, assim como pensamento critico e decisão, foram algo que sempre quis ter sob a minha posse.

### 1.3 Funcionalidades do Claude Utilizadas

| Funcionalidade | Contexto de Utilização | Frequência |
|---|---|---|
| Chat conversacional | Orientação técnica, conceitos Django, depuração | Todas as 12 sessões |
| Projecto Claude | Ficheiros de contexto partilhados entre chats | Todas as sessões |
| Claude in Chrome | Acesso ao repositório GitHub para verificar código já feito por mim | Sessões 6 e 7 |
| Revisão de ficheiros | Revisão de documentos Word (relatório, manual) criados por mim | Sessões 8-12 |
| Pesquisa Web | Investigação de boas práticas académicas de arquitectura e desenho de software| Sessão 8 |
| Memória | Preferências persistentes entre sessões (tratamento informal) | A partir da sessão 6 |

---

## 2. Comentário à System Prompt

### 2.1 Abordagem Adoptada

Ao contrário de uma system prompt tradicional (um bloco fixo de instruções que define o comportamento da IA), a estratégia adoptada neste projecto foi a utilização de um **ficheiro de contexto evolutivo** que funcionou como system prompt dinâmica.

O ficheiro `CONTEXTO_DOMUSSHELF.md` foi criado na segunda sessão de trabalho e evoluiu ao longo de **8 versões** (v1 a v8) durante todo o desenvolvimento. Era anexado no início de cada nova conversa com o Claude, servindo como "instruções de arranque" que definiam:

- **Identidade do projecto:** nome, aluno, disciplina, professor e universidade
- **Estado actual:** fases concluídas, ficheiros existentes, funcionalidades implementadas
- **Decisões técnicas tomadas:** linguagem, framework, base de dados, tema visual, código
- **Conceitos aprendidos:** lista cumulativa de conceitos Django dominados
- **Próximos passos:** orientação para o trabalho da sessão seguinte

### 2.2 Vantagens desta Abordagem

A principal vantagem face a uma system prompt estática é que o ficheiro acompanhou a minha evolução, assim como a do projecto. Na versão 1 continha pouco mais do que o meu planeamento; na versão 8 continha o registo completo de 12 sessões, todos os conceitos Django aprendidos, a estrutura completa do projecto, e até problemas conhecidos e suas soluções.

Os ficheiros do Projecto Claude (email com enunciado do professor, guião aprovado) funcionaram como contexto complementar permanente, garantindo que a IA nunca perdia de vista os requisitos académicos originais.

---

## 3. Sumário das Prompts Utilizadas

### 3.1 Tipologia de Prompts

| Tipo | Exemplo | Sessões |
|---|---|---|
| Brainstorming | "Quero a tua opinião crítica e recomendações sobre um projecto de faculdade e da ideia que tenho..." | 1-2 |
| Implementação guiada | "Ajuda-me com a Fase 8. Acho que a estratégia deve ser..." | 3-7 |
| Depuração | "Fiz update ao MacOS e estou a ter erros no ambiente virtual." | 3-7 |
| Verificação | "Confirma o ficheiro que criei no github em vez de começares do zero." | 4-5 |
| Documentação | "Que alterações recomendas à seguinte Estrutura de Relatório?" | 8-12 |
| Revisão crítica | "Finalizei todo o Projecto. Faz uma verificação total final no github." | 10-12 |



## 4. Crítica ao Output da IA

A utilização da IA não foi um processo passivo de aceitação de respostas. Ao longo do projecto, identifiquei múltiplas situações em que o output estava incorrecto, incompleto ou podia ser melhorado.

### 4.1 O Que Foi Útil

**Explicação de conceitos Django:** a IA explicou de forma clara conceitos como herança de templates, decoradores, ModelForms, context processors e o padrão MTV. Cada conceito foi explicado no momento em que era necessário, integrado no contexto prático do projecto.

**Estruturação do projecto:** a organização em fases incrementais (0 a 10) permitiu gerir a complexidade e manter o foco. Cada sessão tinha objectivos claros e entregáveis concretos, em paralelo do que eu ia fazendo, daí ter optado pela não utilização do Claude Code e usar apenas o Claude Desktop.

**Boas práticas de segurança:** a IA insistiu consistentemente na filtragem por utilizador em todas as views, garantindo isolamento de dados. Também sugeriu o uso de `select_related` para optimização de queries.

### 4.2 O Que Estava Errado ou Limitado

**Exemplo 1 — Instruções baseadas em suposições (Sessão 4):** durante a implementação do CRUD de embalagens, a IA instruiu-me a alterar o ficheiro `base.html` para corrigir URLs da navbar. Após vários erros que a IA cometeu, eu próprio corrigi e enviei à IA, ao que esta admitiu: "O ficheiro base.html já está correcto! Eu estava a basear-me em screenshots parciais e a assumir coisas erradas." Este caso demonstra que a IA por vezes opera com base em presunções em vez de factos verificados e assim foi importante eu ter o controlo de tudo o que era executado e não apenas deixar que Agentes IA o fizessem por mim.

**Exemplo 2 — Erro de import (Sessão 5):** a IA instruiu para importar o modelo `Preferencias` a partir do ficheiro `forms.py` em vez de `models.py`, causando um erro que impedia a aplicação de arrancar. Eu detectei que fazia com que a aplicação tivesse "rebentado" e confrontou a IA, que reconheceu o erro. Este tipo de erro, embora simples de corrigir, poderia ser desastroso para um programador que confiasse cegamente no output.

**Exemplo 3 — Inconsistência visual não detectada (Sessão 4):** Detectei sozinho que o badge verde de "Dentro da validade" aparecia na versão mobile mas não na versão desktop da lista de embalagens. Esta inconsistência, criada pela própria IA ao criar os templates, não foi identificada pela IA até eu apontar.

### 4.3 Verificação de Factos

A verificação da informação fornecida pela IA foi feita através de múltiplas fontes:

**Documentação oficial do Django:** todas as sugestões de código e padrões foram cruzadas com a documentação oficial em docs.djangoproject.com, conforme recomendado pelo professor.

**Django Girls Tutorial:** utilizado como referência complementar por recomendação do professor, serviu para validar a abordagem pedagógica da IA em relação aos conceitos básicos do Django.

**Teste empírico:** cada pedaço de código foi testado manualmente após implementação, tanto no desktop como em modo responsivo (Safari Responsive Design Mode). Esta abordagem permitiu detectar erros como os descritos nos exemplos acima.



## 5. Reflexão Pessoal


### 5.1 Decisões sobre Uso Extensivo vs. Limitado

A decisão de utilizar a IA de forma controlada, através de conversação guiada em vez de geração automática de código, revelou-se acertada para o contexto académico deste projecto. As áreas onde a IA foi mais utilizada (explicação de conceitos, estruturação de fases, depuração) são as áreas onde o valor acrescentado era maior sem comprometer a aprendizagem. As áreas onde foi deliberadamente limitada (execução de código, testes, gestão de versões) são as áreas onde a prática manual era essencial para a compreensão.