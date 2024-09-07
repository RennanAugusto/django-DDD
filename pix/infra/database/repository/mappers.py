from pix.domain.entity import Investimento
from pix.infra.database.models.investimento import  InvestimentoModel


class InvestimentoMapper:
    def to_entity(self, investimento_model: InvestimentoModel) -> Investimento:
        if investimento_model is None:
            return None

        return Investimento.new(investimento_model.id, investimento_model.valor_investimento, investimento_model.valor_retorno)

    def to_model(self, investimento_entity: Investimento) -> InvestimentoModel:
        if investimento_entity.id == 0:
            return InvestimentoModel(valor_investimento=investimento_entity.valor_investimento, valor_retorno=investimento_entity.valor_retorno)
        else:
            return InvestimentoModel(id=investimento_entity.id,valor_investimento=investimento_entity.valor_investimento,
                                     valor_retorno=investimento_entity.valor_retorno)