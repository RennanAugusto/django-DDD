from pix.domain.entity import Investimento
from pix.domain.repository import IInvestimentoRepository
from pix.infra.database.models.investimento import InvestimentoModel
from pix.infra.database.repository.mappers import InvestimentoMapper


class InvestimentoRepository(IInvestimentoRepository):
    def __init__(self):
        self.investimento_mapper: InvestimentoMapper = InvestimentoMapper()

    def get_by_id(self, id: int) -> Investimento:
        return self.investimento_mapper.to_entity(InvestimentoModel.objects.filter(id=id).first())

    def get_all(self) -> list[Investimento]:
        result: list[Investimento] = []
        investimentos = InvestimentoModel.objects.all()

        for investimento in investimentos:
            result.append(self.investimento_mapper.to_entity(investimento))

        return result

    def save(self, entity: Investimento) -> None:
        investimento_model: InvestimentoModel = self.investimento_mapper.to_model(entity)
        investimento_model.save()
        entity.id = investimento_model.id

    def delete(self, id: int) -> None:
        InvestimentoModel.objects.get(id=id).delete()