from sqlalchemy.orm import Session
from pwdlib import PasswordHash

from app.models import Usuario
from app.schemas import UsuarioBase

pwd_context = PasswordHash.recommended()


def get_usuarios(db: Session):
    usuarios_model: list[type[Usuario]] = db.query(Usuario).all()
    return usuarios_model


def get_usuario(usuario_id, db: Session):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()


def create_usuario(db: Session, usuario: UsuarioBase):
    senhaHash = pwd_context.hash(usuario.senha)
    usuario_model = Usuario(username=usuario.username, email=usuario.email,
                            senha=senhaHash)
    db.add(usuario_model)
    db.commit()
    db.refresh(usuario_model)
    return usuario_model.id
