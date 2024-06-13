from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas import UsuarioBase
from app.database import SessionLocal
from app.repository import usuario
from app.models import Usuario


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


@router.get("/{id}", tags=["usuario"])
def get_usuario(id, db: Session = Depends(get_db)):
    retorno = usuario.get_usuario(id, db=db)
    return retorno


@router.post("/", tags=["usuario"])
def post_usuario(usuario_create: UsuarioBase, db: Session = Depends(get_db)):
    db_user = db.query(Usuario).filter(Usuario.email == usuario_create.email).first()
    if db_user:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Email already exists',
        )
    usuario_retorno = usuario.create_usuario(db=db, usuario=usuario_create)
    return usuario_retorno
