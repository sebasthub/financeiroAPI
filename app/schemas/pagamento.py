from pydantic import BaseModel
from datetime import datetime
from .parcela import ParcelaBase
from .categoria import CategoriaBase


class PagamentoBase(BaseModel):
    id: int
    nome: str
    descricao: str
    data_lancamento: datetime
    categoria: CategoriaBase
    parcelas: list[ParcelaBase]


class PagamentoCreate(BaseModel):
    nome: str
    descricao: str
    data_lancamento: datetime
    valor: float
    categoria_id: int
    qtd_parcelas: int


class PagamentoGet(BaseModel):
    id: int
    nome: str
    descricao: str
    data_lancamento: datetime
    categoria: CategoriaBase
    valor: float
