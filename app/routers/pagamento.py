from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas import PagamentoBase, PagamentoCreate
from app.database import SessionLocal
from app.repository import pagamento


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.get("/", response_model=list[PagamentoBase], tags=["pagamento"])
def get_pagamentos(db: Session = Depends(get_db)):
    pagamentos = pagamento.get_pagamentos(db=db)
    return pagamentos


@router.get("/{id}", response_model=PagamentoBase, tags=["pagamento"])
def get_pagamento(id: int, db: Session = Depends(get_db)):
    retorno = pagamento.get_pagamento(id, db=db)
    return retorno


@router.post("/", tags=["pagamento"])
def post_pagamento(pagamento_create: PagamentoCreate, db: Session = Depends(get_db)):
    pagamento_retorno = pagamento.create_pagamento(db=db,pagamento=pagamento_create)
    return pagamento_retorno
