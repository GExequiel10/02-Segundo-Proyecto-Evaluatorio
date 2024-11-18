from datetime import datetime

from pydantic import BaseModel

from .user_schemas import UserResponse


class NewProductRequest(BaseModel):
    name: str = 'new product'
    brand: str = 'generic'
    stock: int = 1
    price: int = 1
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
    stock: int
    price: int
    description: str = ''
    user_id: int
    owner: UserResponse
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
