# Atividade prática | Desenvolvimento de agente inteligente
  
**Proposta:** Desenvolver um agente inteligente utilizando `create_agent()` do
LangChain, aplicando os principais blocos de construção de agentes estudados 
durante as aulas. 
**Entrega:** Código do agente e evidências dos testes (arquivo `avaliacoes.csv`
e cópia do terminal do VS Code com as interações realizadas)

## Objetivo

Desenvolver um agente inteligente capaz de **avaliar programas Python submetidos por
estudantes**, considerando o enunciado e os critérios de avaliação de uma atividade.
O agente deverá selecionar e executar ferramentas previamente implementadas,
produzir uma avaliação estruturada e registrar os resultados.

**Atenção:** nesta atividade, não é necessário implementar novas ferramentas,
criar a interface gráfica ou modificar as bibliotecas auxiliares: o foco é a **lógica
de orquestração do agente**.

## Arquivos e responsabilidades

Os seguintes arquivos são fornecidos:

- `atividades.py`: ferramentas `ler_solucao`, `listar_submissoes` e `consultar_atividade`;
- `registros.py`: ferramenta `registrar_avaliacao`, que grava dados em CSV;
- `modelos.py`: modelos Pydantic `Criterio` e `Avaliacao`;
- `atividade01.txt`: arquivo com enunciado e rubrica de exemplo;
- `aluno10x.py`: arquivos com códigos fictícios para teste.

**Arquivo a desenvolver:** `agente.py`. Não altere os arquivos-base.

## Requisitos funcionais

1. Criar o agente com `create_agent()` e um LLM com suporte à chamada de ferramentas.
2. Redigir um `system_prompt` que oriente o fluxo de avaliação, a utilização
   adequada de cada ferramenta e o formato dos resultados.
3. Quando houver solicitação de **avaliação de um arquivo específico**, consultar
   o enunciado/rubrica e ler **somente** o arquivo indicado, sem chamar
   `listar_submissoes` desnecessariamente.
4. Quando o usuário solicitar a **listagem**, usar `listar_submissoes` e
   apresentar os nomes disponíveis, sem avaliar automaticamente.
5. Quando solicitar **avaliação de todas as submissões**, usar
   `listar_submissoes` e avaliar cada arquivo encontrado.
6. Para cada avaliação: atribuir pontuação por critério, justificar de forma
   objetiva, calcular nota final coerente com a rubrica (0 a 10), produzir
   feedback claro e chamar `registrar_avaliacao` com os dados do modelo `Avaliacao`.
7. Não inventar códigos, critérios ou informações ausentes; comunicar arquivos
   inexistentes, erros das ferramentas e informações insuficientes.
8. **Não executar os códigos submetidos.** A avaliação é feita pela leitura do
   conteúdo da submissão e por análise de conformidade com os critérios.

## Orientações gerais

- Utilize as classes e funções já disponibilizadas.
- A rubrica de exemplo está em `atividades/atividade01.txt`. Para os testes,
  informe explicitamente esse arquivo, como em:
  `Avalie aluno101.py com base em atividade01.txt.`
- A função de registro recebe uma estrutura aninhada: `Avaliacao` contém
  uma lista de objetos `Criterio`. Observe atentamente os campos requeridos.
- O CSV contém apenas `arquivo`, `nota` e `feedback`. A pontuação de cada
  critério é exibida no terminal, mas não é gravada individualmente no CSV.
- Permitir que o usuário interaja com o agente continuamente pelo terminal,
  formulando diferentes solicitações até encerrar a aplicação com `CTRL + C`
  sejam pressionadas.

## Entrega

- `agente.py` implementado e funcional;
- comentários explicativos sobre as principais instruções implementadas 
  em `agente.py`;
- evidências de execução dos testes, conforme orientado pelo professor.

## Critérios sugeridos de avaliação da atividade

| Critério | Pontuação |
|---|---:|
| Configuração correta do agente e integração das quatro tools | 3,0 |
| Orquestração correta para listagem, avaliação individual e em lote | 3,0 |
| Clareza do código e dos comentários explicativos | 2,0 |
| Apresentação completa dos testes realizados | 2,0 |
| **Total** | **10,0** |
