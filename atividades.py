from pathlib import Path
from langchain_core.tools import tool

@tool
def ler_solucao(arquivo: str) -> str:
  """Lê o código-fonte Python submetido por um estudante"""

  print("@tool: ler_solucao")

  pasta = Path("submissoes").resolve()
  caminho = (pasta / arquivo).resolve()

  if caminho.parent != pasta or caminho.suffix.lower() != ".py":
    return "Arquivo não permitido."

  if not caminho.is_file():
    return "Arquivo não encontrado."

  return caminho.read_text(encoding="utf-8")

@tool
def listar_submissoes() -> list[str]:
  """
    Lista os arquivos Python disponíveis para avaliação.
    Utilize esta ferramenta somente quando o usuário solicitar
    a listagem de submissões ou a avaliação de todas elas.
    Não utilize esta ferramenta quando o usuário informar
    explicitamente o nome do arquivo .py que deseja avaliar.
  """

  print("@tool: listar_submissoes")

  pasta = Path("submissoes")

  arquivos = []

  for arquivo in pasta.glob("*.py"):
    if arquivo.is_file():
      arquivos.append(arquivo.name)

  arquivos.sort()

  return arquivos

@tool
def consultar_atividade(arquivo: str) -> str:
  """Consulta o enunciado e os critérios de avaliação de uma atividade."""

  print("@tool: consultar_atividade")

  pasta = Path("atividades").resolve()
  caminho = (pasta / arquivo).resolve()

  if caminho.parent != pasta or caminho.suffix.lower() != ".txt":
    return "Arquivo não permitido."

  if not caminho.is_file():
    return "Atividade não encontrada."

  return caminho.read_text(encoding="utf-8")