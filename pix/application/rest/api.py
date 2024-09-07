from typing import List

from django.http import HttpResponse
from ninja import Router, NinjaAPI
from pix.domain.entity import Investimento
from pix.domain.services import InvestimentoService
from pix.infra.database.repository.repository import InvestimentoRepository
from pix.presentation.request import PostInvestimento
from pix.presentation.response import InvestimentoSchema, InvestimentoResponse, ErrorSchema

router = Router(tags=["investimento"])
investimento_service = InvestimentoService(InvestimentoRepository())

@router.post("/investimento", response={201: InvestimentoSchema})
def post_investimento(request, body: PostInvestimento):
    investimento = Investimento.new(0, body.valor_investimento, body.valor_retorno)
    investimento_service.post_investimento(investimento)
    return 201, investimento

@router.get("/investimento/{id}", response={200: InvestimentoSchema, 404: ErrorSchema})
def get_investimento(request, id):
    investimento = investimento_service.get_investimento(id)

    if investimento is None:
        return 404, ErrorSchema(error="not found")

    return 200, investimento

@router.get("/investimento", response={200: List[InvestimentoSchema]})
def get_investimentos(request):
    investimentos = investimento_service.get_all_investimentos()
    return 200, investimentos

@router.delete("/investimento/{id}")
def delete_investimento(request, id):
    investimento_service.delete_investimento(id)
    return HttpResponse(status=204)