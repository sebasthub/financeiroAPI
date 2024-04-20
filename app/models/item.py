from datetime import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, DOUBLE
from sqlalchemy.orm import relationship

from app.database import Base


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    image_url = Column(String)
    valor = Column(DOUBLE)
    created_at = Column(DateTime, default=datetime.now())
    pagamento_id = Column(Integer, ForeignKey('pagamento.id'), nullable=True)
    pagamento = relationship('Pagamento')

