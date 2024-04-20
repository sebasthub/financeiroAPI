from fastapi import Depends, FastAPI, HTTPException

from . import models
from app import router
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router.api_router)
