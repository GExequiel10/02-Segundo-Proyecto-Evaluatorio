from typing import Annotated, List

from fastapi import APIRouter, Path, Query

from server.schemas.project_schemas import NewProjectRequest, ProjectResponse, ProjectRequest #TODO
from server.controller import ProjectsController #TODO
from server.exceptions import InternalServerError, NotFound

router = APIRouter(prefix='/products')
router.responses = {
    500: InternalServerError.as_dict(),
}
controller = ProjectsController() #TODO



@router.post(
    '',  # ruta
    status_code=201,
    responses={
        201: {'description': 'Producto creado'},
    },
    description='Crea un producto nuevo pasado por Body Param. Falla si falta alguno de los campos obligatorios.'
)  # POST /projects
async def create(new_project: NewProjectRequest) -> ProjectResponse: #TODO
    # esto seria todo el codigo: retornar la funcion que le corresponde al controlador pasandole un parametro
    return controller.create(new_project) #TODO


@router.get(
    '',  # ruta
    status_code=200,
    responses={
        200: {'description': 'Listado de productos'},
    },
    description='Retorna una lista paginada con los productos del negocio. Si no hay productos para mostrar, retorna una lista vacia.'
)  # GET /projects
async def get_list(limit: Annotated[int, Query(ge=1, le=1000)] = 10, offset: Annotated[int, Query(ge=0)] = 0) -> List[ProjectResponse]: #TODO
    return controller.get_list(limit, offset)


@router.get(
    '/{id}',  # path
    status_code=200,
    responses={
        201: {'description': 'Producto encontrado'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es de tipo valido. Debe ser entero'},
    },
    description='Retorna un producto por ID. Falla si el ID no existe.'
)  # GET BY ID /projects
# con este Path Param valido datos en el endpoint y no en el servidor. Ahorra tiempo
async def get_by_id(id: Annotated[int, Path(ge=1)]) -> ProjectResponse: #TODO
    return controller.get_by_id(id)


@router.patch(
    '/{id}',  # path
    status_code=200,
    responses={
        200: {'description': 'Producto actualizado'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es de tipo valido. Debe ser entero'},
    },
    description='Actualiza un producto con la data del Body Param. Falla si el ID no existe.'
)  # PATCH /projects
async def update(id: Annotated[int, Path(ge=1)], project: ProjectRequest) -> ProjectResponse: #TODO
    return controller.update(id, project) #TODO


@router.delete(
    '/{id}',  # path
    status_code=204,
    responses={
        204: {'description': 'Producto borrado'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es de tipo valido. Debe ser entero'},
    },
    description='Borra un producto a partir del ID pasado por Path Param. Falla si el ID no existe.'
)  # DELETE /projects
async def delete(id: Annotated[int, Path(ge=1)]) -> None:
    controller.delete(id)
