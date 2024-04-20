from pydantic import BaseModel
from datetime import datetime


class ParcelaBase(BaseModel):
    parcela: int
    valor: float
    data: datetime

