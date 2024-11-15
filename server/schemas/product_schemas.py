from datetime import datetime

from pydantic import BaseModel


class NewProductRequest(BaseModel):
    name: str = 'new product'
    brand: str = 'generic'
    stock: int = '1'
    price: int = '1'
    description: str = ''  # Con las '' le damos un valor por defecto


class ProductRequest(BaseModel):
    name: str | None = None
    brand: str | None = None
    stock: int | None = None
    price: int | None = None
    description: str | None = None


class ProductResponse(BaseModel):
    id: int
    name: str = 'new product'
    brand: str = 'generic'
    stock: int = '1'
    price: int = '1'
    description: str = ''
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
