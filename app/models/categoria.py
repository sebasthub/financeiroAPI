from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, DOUBLE

from app.database import Base

class Categoria(Base):
    __tablename__ = 'categoria'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)