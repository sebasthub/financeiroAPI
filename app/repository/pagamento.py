from sqlalchemy.orm import Session, joinedload
from datetime import datetime

from app.models import Pagamento, Parcela
from app.schemas import PagamentoCreate, PagamentoBase, ParcelaBase


def get_parcela(db: Session, id_pagamento: int):
    parcelas_model = db.query(Parcela).filter(Parcela.pagamento_id == id_pagamento)
    parcelas_response: list[ParcelaBase] = []
    for parcela in parcelas_model:
        parcelas_response.append(ParcelaBase(parcela))
    return parcelas_response


def get_pagamentos(db: Session):
    pagamentos_model: list[type[Pagamento]] = db.query(Pagamento).options(joinedload(Pagamento.parcelas), joinedload(Pagamento.categoria)).all()
    return pagamentos_model


def get_pagamento(pagamento_id: int, db: Session):
    return db.query(Pagamento).filter(Pagamento.id == pagamento_id).options(joinedload(Pagamento.parcelas), joinedload(Pagamento.categoria)).first()


def create_pagamento(db: Session, pagamento: PagamentoCreate):
    pagamento_model = Pagamento(nome=pagamento.nome, descricao=pagamento.descricao,
                                data_lancamento=pagamento.data_lancamento, categoria_id=pagamento.categoria_id)
    db.add(pagamento_model)
    db.commit()
    db.refresh(pagamento_model)
    valor: float = pagamento.valor/pagamento.qtd_parcelas
    for i in range(0, pagamento.qtd_parcelas):
        parcela = Parcela(parcela=i, valor=valor, data=datetime.now(),
                          pagamento_id=pagamento_model.id)
        db.add(parcela)
    db.commit()
    return pagamento_model.id
