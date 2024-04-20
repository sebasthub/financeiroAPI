from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from app.database import Base
from app.models import Pagamento


class Parcela(Base):
    __tablename__ = 'parcela'
    id = Column(Integer, primary_key=True, autoincrement=True)
    parcela = Column(Integer, nullable=False)
    valor = Column(Float, nullable=False)
    data = Column(DateTime, nullable=False)
    pagamento_id = Column(Integer, ForeignKey('pagamento.id'))
    pagamento = relationship(Pagamento, back_populates="parcelas")
