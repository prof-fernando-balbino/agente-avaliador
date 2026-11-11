from pydantic import BaseModel, Field

from pydantic import BaseModel, Field

class Criterio(BaseModel):
    descricao: str = Field(description="Nome do critério da rubrica")
    pontuacao: float = Field(
        ge=0,
        description="Pontuação atribuída ao critério"
    )
    justificativa: str = Field(
        description="Justificativa objetiva para a pontuação"
    )

class Avaliacao(BaseModel):
    arquivo: str = Field(description="Nome do arquivo Python avaliado")
    nota: float = Field(ge=0, le=10)
    criterios: list[Criterio]
    feedback: str
