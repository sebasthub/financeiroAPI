from pydantic import BaseModel
from datetime import datetime
from .parcela import ParcelaBase


class PagamentoBase(BaseModel):
    id: int
    nome: str
    descricao: str
    data_lancamento: datetime
    parcelas: list[ParcelaBase]


class PagamentoCreate(BaseModel):
    nome: str
    descricao: str
    data_lancamento: datetime
    valor: float
    qtd_parcelas: int
