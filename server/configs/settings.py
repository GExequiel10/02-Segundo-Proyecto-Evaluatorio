from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API
    PORT: int = 8000
    DEV: bool = False
    
    # JWT
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = 'HS256'
    JWT_EXPIRATION_TIME_MINUTES: int = 60
    
    # External DAta
    PRODUCTS_API: str
    
    #Database
    DB_CONN: str

    # Logging
    DEBUG: bool = False

    # Solo se define una clase dentro de otro cuando solo es importante para la clase padre
    class Config:
        env_file = '.env'
