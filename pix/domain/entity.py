class Investimento():
    id: int
    valor_investimento: float
    valor_retorno: float

    def __init__(self, id, valor_investimento, valor_retorno):
        self.id = id
        self.valor_investimento = valor_investimento
        self.valor_retorno = valor_retorno

    @classmethod
    def new(cls, id: int, valor_investimento: float, valor_retorno: float):
        return cls(id=id, valor_investimento=valor_investimento, valor_retorno=valor_retorno)