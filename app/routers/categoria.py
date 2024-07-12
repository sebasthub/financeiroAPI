from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.repository import categoria as repository
from app.models import Categoria
from app.schemas import CategoriaBase
from app.auth import get_user, User


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.get("/", tags=["categoria"])
def get_categorias(db: Session = Depends(get_db), user: User = Depends(get_user)):
    categoria_resposta = repository.get_categorias(db, user)
    return categoria_resposta


@router.post("/", tags=["categoria"])
def post_pagamento(categoria_body: CategoriaBase, db: Session = Depends(get_db), user: User = Depends(get_user)):
    categoria_retorno = repository.create_catgoria(db=db, categoria=categoria_body, usuario=user)
    return categoria_retorno
