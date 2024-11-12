#Aca usamos herencia
from fastapi import HTTPException


class BaseHTTPException(HTTPException):
    #Atributos de clase
    description: str
    status_code: int
    
    def __init__(self, message: str = '' ):
        super().__init__(status_code=self.status_code, detail=message)
        
    @classmethod   
    def as_dict(cls) -> dict:
        return {'description': cls.description}
         