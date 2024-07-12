from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.database import Base


class Pagamento(Base):
    __tablename__ = 'pagamento'
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(String(50), nullable=False)
    nome = Column(String(255), nullable=False)
    descricao = Column(String(255), nullable=False)
    data_lancamento = Column(DateTime(), nullable=False)
    parcelas = relationship('Parcela', back_populates='pagamento')
    categoria_id = Column(Integer, ForeignKey('categoria.id'))
    categoria = relationship('Categoria')
