from pix.domain.entity import Investimento
import abc


class IInvestimentoRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_by_id(self, id: int) -> Investimento:
        pass

    @abc.abstractmethod
    def get_all(self) -> list[Investimento]:
        pass

    @abc.abstractmethod
    def save(self, entity: Investimento) -> None:
        pass

    @abc.abstractmethod
    def delete(self, id: int) -> None:
        pass