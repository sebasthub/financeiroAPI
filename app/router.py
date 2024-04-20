from fastapi import APIRouter

from app.routers import pagamento

api_router = APIRouter()

api_router.include_router(pagamento.router, prefix="/pagamento")
