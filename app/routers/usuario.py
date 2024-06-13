from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas import UsuarioBase
from app.database import SessionLocal
from app.repository import usuario


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.get("/", tags=["usuario"])
def get_usuarios(db: Session = Depends(get_db)):
    usuarios = usuario.get_usuarios(db=db)
    return usuarios


@router.get("/{id}", tags=["pagamento"])
def get_usuario(id, db: Session = Depends(get_db)):
    retorno = usuario.get_usuario(id, db=db)
    return retorno


@router.post("/", tags=["pagamento"])
def post_usuario(usuario_create: UsuarioBase, db: Session = Depends(get_db)):
    usuario_retorno = usuario.create_usuario(db=db, usuario=usuario_create)
    return usuario_retorno
