# Atividade: agente inteligente avaliador de códigos Python

OS arquivos disponíveis formam a base do projeto e devem ser organizados
conforme indicado na seção **Estrutura**, logo abaixo. As quatro ferramentas
e os modelos de dados já estão prontos. Você deve implementar apenas 
`agente.py`, para que o agente orquestre essas ferramentas e avalie 
exercícios de programação de acordo com uma rubrica.

> **Importante:** as submissões fornecidas são apenas ilustrativas.
> Não execute código submetido para avaliá-lo; realize análise estática de seu conteúdo.

## Estrutura

```text
agente_avaliador/
├── agente.py                  # EDITAR: sua implementação
├── atividades.py              # Tool: ler, listar e consultar atividade (não editar)
├── modelos.py                 # Modelos Pydantic (não editar)
├── registros.py               # Tool: registrar avaliação em CSV (não editar)
├── atividades/
│   └── atividade01.txt       # Enunciado e rubrica de exemplo
├── submissoes/
│   ├── aluno101.py           # Exemplo fictício
│   ├── aluno102.py           # Exemplo fictício
│   └── aluno103.py           # Exemplo fictício
├── data/
├── requirements.txt
├── .env.
├── .gitignore
├── README.md
└── ENUNCIADO.md
```

## Preparação (PowerShell no Windows)

1. Organize a pasta de projeto, abra-a no VS Code, crie um ambiente virtual e
   ative-o:

   ```powershell
   py -m venv venv
   ```
   
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

2. Instale as dependências:

   ```powershell
   python -m pip install -r requirements.txt
   ```

3. Crie um arquivo `.env` na pasta principal do projeto e configure a chave de API
   correspondente ao modelo de linguagem escolhido. Para utilizar o Groq, defina 
   a variável `GROQ_API_KEY`.

4. Implemente `agente.py`, execute-o e teste para verificar se o comportamento do
   agente está de acordo com o esperado. Há sugestões de testes na seção
   **Testes mínimos**, logo abaixo.

## Ferramentas já implementadas

| Ferramenta | Entrada | Finalidade |
|---|---|---|
| `ler_solucao` | nome do arquivo `.py` | Lê o código em `submissoes/` |
| `listar_submissoes` | nenhuma | Lista os arquivos `.py` em `submissoes/` |
| `consultar_atividade` | nome do arquivo `.txt` | Lê enunciado e rubrica em `atividades/` |
| `registrar_avaliacao` | objeto `Avaliacao` | Registra arquivo, nota e feedback em `data/avaliacoes.csv` |

`modelos.py` define `Criterio(descricao, pontuacao, justificativa)` e
`Avaliacao(arquivo, nota, criterios, feedback)`. O agente deve fornecer
essa estrutura ao chamar `registrar_avaliacao`.

## Testes mínimos

- `Liste as submissões disponíveis.`
- `Avalie aluno101.py com base em atividade01.txt.`
- `Avalie aluno102.py com base em atividade01.txt.`
- `Avalie todas as submissões disponíveis conforme atividade01.txt.`
- `Explique por que a segunda submissão perdeu pontos.`

Consulte **[ENUNCIADO.md](ENUNCIADO.md)** para os requisitos completos de entrega.