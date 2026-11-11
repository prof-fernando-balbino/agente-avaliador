import csv
from pathlib import Path
from modelos import Avaliacao
from langchain_core.tools import tool

@tool
def registrar_avaliacao(avaliacao: Avaliacao) -> str:
  """
    Registra o resultado de uma avaliação em um arquivo csv.
  """

  exibir_avaliacao(avaliacao)

  print("@tool: registrar_avaliacao")

  caminho = Path("data/avaliacoes.csv")

  caminho.parent.mkdir(parents=True, exist_ok=True)

  arquivo_existe = caminho.exists()

  with open(caminho, mode="a", newline="", encoding="utf-8") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=["arquivo", "nota", "feedback"])

    if not arquivo_existe:
      escritor.writeheader()

    escritor.writerow({
      "arquivo": avaliacao.arquivo,
      "nota": avaliacao.nota,
      "feedback": avaliacao.feedback
    })

  return f"Avaliação de {avaliacao.arquivo} registrada com sucesso."

def exibir_avaliacao(avaliacao: Avaliacao):
  print("\n***********************************************")
  print("Arquivo:", avaliacao.arquivo)
  print("Nota:", avaliacao.nota)
  print("Feedback:", avaliacao.feedback, "\n")

  for criterio in avaliacao.criterios:
      print("Critério:", criterio.descricao)
      print("Pontuação:", criterio.pontuacao)
  print("\n***********************************************")
