import logging
from typing import List

from server.schemas.product_schemas import NewProductRequest, ProductResponse, ProductRequest
from server.exceptions import BaseHTTPException, InternalServerError, Forbidden
from server.service import ProductsService
from server.enums import ADMIN_ROLES
from server.schemas.auth_schemas import DecodedJwt


logger = logging.getLogger(__name__)


class ProductsController:
    def __init__(self):
        self.service = ProductsService()

    def create(self, new_product: NewProductRequest, user_id: int) -> ProductResponse:
        try:
            logger.debug(
                f'Crear producto {new_product.name} {new_product.brand}')
            return self.service.create(new_product, user_id)
        except BaseHTTPException as ex:
            logger.error(
                f'Error al procesar request, status code {ex.status_code}: {ex.description}')
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(
                f'Error no contemplado en {__name__}.create():' + str(ex))
            raise InternalServerError()

    # No definimos valores por defecto de limit y offset porque ya esta validado por la ruta
    def get_list(self, limit: int, offset: int, user_id: int) -> List[ProductResponse]:
        try:
            return self.service.get_list(limit, offset, user_id)
        except BaseHTTPException as ex:
            # logger.error(f'Error al procesaar request, status code {ex.status_code}: {ex.description}') #
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(
                f'Error no contemplado en {__name__}.get_list():' + str(ex))
            raise InternalServerError()

    def get_by_id(self, id: int, token: DecodedJwt) -> ProductResponse:
        try:
            logger.debug(f'Buscar producto #{id}')
            product = self.service.get_by_id(id)
            self.__check_access(product.user_id, token)
            return product
        except BaseHTTPException as ex:
            # logger.error(f'Error al procesaar request, status code {ex.status_code}: {ex.description}') #
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(
                f'Error no contemplado en {__name__}.get_by_id():' + str(ex))
            raise InternalServerError()

    def update(self, id: int, new_data: ProductRequest, token: DecodedJwt) -> ProductResponse:
        try:
            self.get_by_id(id, token)
            return self.service.update(id, new_data)
        except BaseHTTPException as ex:
            # logger.error(f'Error al procesaar request, status code {ex.status_code}: {ex.description}') #
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(
                f'Error no contemplado en {__name__}.update():' + str(ex))
            raise InternalServerError()

    def delete(self, id: int, token: DecodedJwt) -> None:
        try:
            self.get_by_id(id, token)
            self.service.delete(id)
        except BaseHTTPException as ex:
            # logger.error(f'Error al procesaar request, status code {ex.status_code}: {ex.description}') #
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(
                f'Error no contemplado en {__name__}.delete():' + str(ex))
            raise InternalServerError()

    def __handler_http_exception(self, ex: BaseHTTPException):
        if ex.status_code >= 500:
            logger.critical(
                f'Error en el servidor con status code {ex.status_code}:{ex.description}')
        else:
            logger.error(f'Error {ex.status_code}:{ex.description}')
        raise ex
    
    def __check_access(self, owner_id:int, token:DecodedJwt)-> None:
        if (owner_id != token.user_id) and (token.role not in ADMIN_ROLES):
            raise Forbidden ('El usuario no tiene acceso a este proyecto')
