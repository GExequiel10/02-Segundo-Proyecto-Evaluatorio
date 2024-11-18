from .base_http_exception import BaseHTTPException


class BadRequest(BaseHTTPException):
    description = 'Algo salio mal con el request enviado por el cliente'
    status_code = 400
    
class NotFound(BaseHTTPException):
    description = 'Recurso no encontrado'
    status_code = 404
    
class Unauthorized(BaseException):
    description = 'El usuario debe estar logeado'
    status_code = 401
    
class Forbidden(BaseException):
    description = 'El usuario no tiene acceso a este recurso'
    status_code = 403