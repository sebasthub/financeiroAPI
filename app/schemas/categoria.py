from pydantic import BaseModel


class CategoriaBase(BaseModel):
    name: str


class CategoriaGet(CategoriaBase):
    id: int

    class Config:
        from_attributes = True
