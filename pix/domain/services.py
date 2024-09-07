from pix.domain.entity import Investimento
from pix.domain.repository import IInvestimentoRepository


class InvestimentoService:
    def __init__(self, investimento_repository: IInvestimentoRepository):
        self.investimento_repository = investimento_repository

    def post_investimento(self, investimento: Investimento) -> Investimento:
        #Alguma regra de negocio
        self.investimento_repository.save(investimento)
        return investimento

    def get_all_investimentos(self) -> list[Investimento]:
        return self.investimento_repository.get_all()

    def get_investimento(self, id: int) -> Investimento:
        return self.investimento_repository.get_by_id(id)

    def delete_investimento(self, id: int) -> None:
        self.investimento_repository.delete(id)