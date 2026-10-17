from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int | None = None
    nombre: str = Field(min_length=5)
    descripcion: str | None = None
    precio: float = Field(gt=0)
    stock: int = Field(ge=0)