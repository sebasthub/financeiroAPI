from pydantic import BaseModel
import uuid


class UsuarioBase(BaseModel):
    username: str
    email: str
    senha: str
