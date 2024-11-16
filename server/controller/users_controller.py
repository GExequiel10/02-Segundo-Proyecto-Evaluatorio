import logging
from typing import List

from server.schemas.user_schemas import NewUserRequest, UserRequest, UserResponse
from server.exceptions import BaseHTTPException, InternalServerError
from server.service import UsersService


logger = logging.getLogger(__name__)


class UsersController:
    def __init__(self):
        self.service = UsersService()

    def create(self, new_user: NewUserRequest) -> UserResponse:
        try:
            logger.debug(
                f'Crear usuario {new_user.username}')
            return self.service.create(new_user)
        except BaseHTTPException as ex:
            logger.error(
                f'Error al procesar request, status code {ex.status_code}: {ex.description}')
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(
                f'Error no contemplado en {__name__}.create():' + str(ex))
            raise InternalServerError()


    def get_list(self, limit: int, offset: int) -> List[UserResponse]:
        try:
            return self.service.get_list(limit, offset)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(
                f'Error no contemplado en {__name__}.get_list():' + str(ex))
            raise InternalServerError()

    def get_by_id(self, id: int) -> UserResponse:
        try:
            logger.debug(f'Buscar usuario #{id}')
            return self.service.get_by_id(id)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(
                f'Error no contemplado en {__name__}.get_by_id():' + str(ex))
            raise InternalServerError()

    def update(self, id: int, new_data: UserRequest) -> UserResponse:
        try:
            return self.service.update(id, new_data)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(
                f'Error no contemplado en {__name__}.update():' + str(ex))
            raise InternalServerError()

    def delete(self, id: int) -> None:
        try:
            self.service.delete(id)
        except BaseHTTPException as ex:
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
