from datetime import datetime

from pydantic import BaseModel, EmailStr


class NewUserRequest(BaseModel):
    username: str
    password: str
    email: EmailStr
 

class UserRequest(BaseModel):
    username: str | None = None
    password: str | None = None
    email: EmailStr | None = None
    
    
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    
    # class Config:
    #     from_attributes = True
