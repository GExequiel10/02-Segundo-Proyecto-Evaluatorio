from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from .base_model import BaseModel

class UserModel(BaseModel):
    __tablename__ = 'users'
    
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    
