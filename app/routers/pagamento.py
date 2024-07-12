from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import User, get_user
from app.schemas import PagamentoBase, PagamentoCreate, PagamentoGet, CategoriaBase
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


@router.get("/", response_model=list[PagamentoGet], tags=["pagamento"])
def get_pagamentos(db: Session = Depends(get_db), usuario: User = Depends(get_user)):
    pagamentos = pagamento.get_pagamentos(db=db, usuario=usuario)
    list_get: list[PagamentoGet] = []
    for pg in pagamentos:
        acm = 0
        for parcela in pg.parcelas:
            acm += parcela.valor
        get = PagamentoGet(id=pg.id, nome=pg.nome, descricao=pg.descricao, data_lancamento=pg.data_lancamento,
                           categoria=CategoriaBase(name=pg.categoria.name), valor=acm)
        list_get.append(get)
    return list_get


@router.get("/{id}", tags=["pagamento"])
def get_pagamento(id: int, db: Session = Depends(get_db), usuario: User = Depends(get_user)):
    retorno = pagamento.get_pagamento(id, db=db, usuario=usuario)
    if retorno is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return retorno


@router.post("/", tags=["pagamento"])
def post_pagamento(pagamento_create: PagamentoCreate, db: Session = Depends(get_db), usuario: User = Depends(get_user)):
    pagamento_retorno = pagamento.create_pagamento(db=db, pagamento=pagamento_create, usuario=usuario)
    return pagamento_retorno
