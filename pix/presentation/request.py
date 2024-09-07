from ninja import Schema


class PostInvestimento(Schema):
    valor_investimento: float
    valor_retorno: float