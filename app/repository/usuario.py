from sqlalchemy.orm import Session, joinedload
from datetime import datetime

from app.models import Usuario
from app.schemas import UsuarioBase


def get_usuarios(db: Session):
    usuarios_model: list[type[Usuario]] = db.query(Usuario).all()
    return usuarios_model


def get_usuario(usuario_id, db: Session):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()


def create_usuario(db: Session, usuario: UsuarioBase):
    usuario_model = Usuario(username=usuario.username, email=usuario.descricao,
                            senha=usuario.data_lancamento)
    db.add(usuario_model)
    db.commit()
    db.refresh(usuario_model)
    return usuario_model.id
