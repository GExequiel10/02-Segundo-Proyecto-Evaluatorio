from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey

from .base_model import BaseModel

class ProductModel(BaseModel):
    __tablename__ = 'products'
    
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    brand: Mapped[str] = mapped_column(String(50), nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    price: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    
    # Foreign Key
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    
    owner = relationship('UserModel', back_populates='products', lazy='joined') # agrego lazy para las relaciones
    
    def to_dict(self):
        response = super().to_dict()
        if self.owner:
            response['owner'] = self.owner.to_dict()
        return response
