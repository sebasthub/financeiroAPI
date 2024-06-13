from pydantic import BaseModel
import uuid

class UsuarioBase(BaseModel):
    usuario: str
    email: str
    senha: str