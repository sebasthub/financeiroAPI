from sqlalchemy.orm import Session, joinedload

from app.models import Categoria
from app.schemas import CategoriaBase


def get_categorias(db: Session):
    categorias_model: list[type[Categoria]] = db.query(Categoria).all()
    return categorias_model


def create_catgoria(db: Session, categoria: CategoriaBase):
    categoria_model = Categoria(name=categoria.name)
    db.add(categoria_model)
    db.commit()
    db.refresh(categoria_model)
    db.commit()
    return categoria_model.id