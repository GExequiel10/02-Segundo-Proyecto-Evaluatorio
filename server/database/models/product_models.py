from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer

from .base_model import BaseModel

class ProductModel(BaseModel):
    __tablename__ = 'products'
    
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    brand: Mapped[str] = mapped_column(String(50), nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
