from ninja import Schema
from pix.domain.entity import Investimento


class InvestimentoSchema(Schema):
    id: int
    valor_investimento: float
    valor_retorno: float


class ErrorSchema(Schema):
    error: str


class InvestimentoResponse(Schema):
    investimento: InvestimentoSchema

    @classmethod
    def build(cls, investimento: Investimento) -> dict:
        return cls(invesetimento=InvestimentoSchema(id=investimento.id, valor_investimento=investimento.valor_investimento,
                                                    valor_retorno=investimento.valor_retorno)).model_dump()