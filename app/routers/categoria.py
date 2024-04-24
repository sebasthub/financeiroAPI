from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.repository import categoria as repository
from app.models import Categoria
from app.schemas import CategoriaBase



# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()

@router.get("/", tags=["categoria"])
def get_categorias(db: Session = Depends(get_db)):
    categoria_resposta = repository.get_categorias(db)
    return categoria_resposta


@router.post("/", tags=["categoria"])
def post_pagamento(categoria_body: CategoriaBase, db: Session = Depends(get_db)):
    categoria_retorno = repository.create_catgoria(db=db,categoria=categoria_body)
    return categoria_retorno