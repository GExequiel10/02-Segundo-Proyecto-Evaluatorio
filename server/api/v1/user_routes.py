from typing import Annotated, List

from fastapi import APIRouter, Path, Query

from server.schemas.user_schemas import NewUserRequest, UserResponse, UserRequest
from server.controller import UsersController
from server.exceptions import InternalServerError, NotFound

router = APIRouter(prefix='/users')
router.responses = {
    500: InternalServerError.as_dict(),
}
controller = UsersController()


@router.post(
    '',  # ruta
    status_code=201,
    responses={
        201: {'description': 'Usuario creado'},
    },
    description='Crea un usuario nuevo pasado por Body Param. Falla si falta alguno de los campos obligatorios.'
)  # POST /users
async def create(new_user: NewUserRequest) -> UserResponse:
    return controller.create(new_user)


@router.get(
    '',  # ruta
    status_code=200,
    responses={
        200: {'description': 'Listado de usuarios'},
    },
    description='Retorna una lista paginada con los usuarios del negocio. Si no hay usuario para mostrar, retorna una lista vacia.'
)  # GET /users
async def get_list(limit: Annotated[int, Query(ge=1, le=1000)] = 10, offset: Annotated[int, Query(ge=0)] = 0) -> List[UserResponse]:
    return controller.get_list(limit, offset)


@router.get(
    '/{id}',  # path
    status_code=200,
    responses={
        201: {'description': 'Usuario encontrado'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es de tipo valido. Debe ser entero'},
    },
    description='Retorna un usuario por ID. Falla si el ID no existe.'
)  # GET BY ID /users
async def get_by_id(id: Annotated[int, Path(ge=1)]) -> UserResponse:
    return controller.get_by_id(id)


@router.patch(
    '/{id}',  # path
    status_code=200,
    responses={
        200: {'description': 'Usuario actualizado'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es de tipo valido. Debe ser entero'},
    },
    description='Actualiza la informacion de un usuario con la data del Body Param. Falla si el ID no existe.'
)  # PATCH /users
async def update(id: Annotated[int, Path(ge=1)], user: UserRequest) -> UserResponse:
    return controller.update(id, user)


@router.delete(
    '/{id}',  # path
    status_code=204,
    responses={
        204: {'description': 'Usuario borrado'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es de tipo valido. Debe ser entero'},
    },
    description='Elimina un usuario a partir del ID pasado por Path Param. Falla si el ID no existe.'
)  # DELETE /users
async def delete(id: Annotated[int, Path(ge=1)]) -> None:
    controller.delete(id)
