from .base_http_exceptions import BaseHTTPException


class BadRequest(BaseHTTPException):
    description = 'Algo salio mal con el request enviado por el cliente'
    status_code = 400
    
class NotFound(BaseHTTPException):
    description = 'Recurso no encontrado'
    status_code = 404