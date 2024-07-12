from sqlalchemy.orm import Session, joinedload

from app.auth import User
from app.models import Categoria
from app.schemas import CategoriaBase, CategoriaGet


def get_categorias(db: Session, usuario: User):
    categorias_model: list[type[Categoria]] = db.query(Categoria).filter_by(usuario_id=usuario.sub).all()
    categorias_model_maped = [CategoriaGet.model_validate(obj) for obj in categorias_model]
    return categorias_model_maped


def create_catgoria(db: Session, categoria: CategoriaBase, usuario: User):
    categoria_model = Categoria(name=categoria.name, usuario_id=usuario.sub)
    db.add(categoria_model)
    db.commit()
    db.refresh(categoria_model)
    db.commit()
    return CategoriaGet.model_validate(categoria_model)
