from fastapi import APIRouter

from app.routers import pagamento, categoria

api_router = APIRouter()

api_router.include_router(pagamento.router, prefix="/pagamento")
api_router.include_router(categoria.router, prefix="/categoria")
