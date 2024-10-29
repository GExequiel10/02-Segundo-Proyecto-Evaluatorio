from typing import Annotated, List

from fastapi import APIRouter, Path, Query

from server.schemas.project_schemas import NewProjectRequest, ProjectResponse, ProjectRequest
from server.controller import ProjectsController
from server.exceptions import InternalServerError, NotFound

router = APIRouter(prefix='/projects')
router.responses = {
    500: InternalServerError.as_dict(),
}
controller = ProjectsController()


@router.post(
    '',  # ruta
    status_code=201,
    responses={
        201: {'description': 'Proyecto creado'},
    },
    description='Crea un proyecto nuevo pasado por Body Param. Falla si alguno de los campos obligatorios falta.'
)  # POST /projects
async def create(new_project: NewProjectRequest) -> ProjectResponse:
    # esto seria todo el codigo: retornar la funcion que le corresponde al controlador pasandole un parametro
    return controller.create(new_project)


@router.get(
    '',  # ruta
    status_code=200,
    responses={
        200: {'description': 'Listado de proyectos'},
    },
    description='Retorna una lista pagina con los proyectos. Si no hay proyectos, retorna una lista vacia.'
)  # GET /projects
async def get_list(limit: Annotated[int, Query(ge=1, le=1000)] = 10, offset: Annotated[int, Query(ge=0)] = 0) -> List[ProjectResponse]:
    return controller.get_list(limit, offset)


@router.get(
    '/{id}',  # path
    status_code=200,
    responses={
        201: {'description': 'Proyecto encontrado'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es de tipo valido. Debe ser entero'},
    },
    description='Devuelve un proyecto por ID. Falla si el ID no existe.'
)  # GET BY ID /projects
# con este Path Param valido datos en el endpoint y no en el servidor. Ahorra tiempo
async def get_by_id(id: Annotated[int, Path(ge=1)]) -> ProjectResponse:
    return controller.get_by_id(id)


@router.patch(
    '/{id}',  # path
    status_code=200,
    responses={
        201: {'description': 'Proyecto actualizado'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es de tipo valido. Debe ser entero'},
    },
    description='Actualiza un proyecto con la data del Body Param. Falla si el ID no existe.'
)  # PATCH /projects
async def update(id: Annotated[int, Path(ge=1)], project: ProjectRequest) -> ProjectResponse:
    return controller.update(id, project)


@router.delete(
    '/{id}',  # path
    status_code=204,
    responses={
        204: {'description': 'Proyecto borrado'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es de tipo valido. Debe ser entero'},
    },
    description='Borra un proyecto a partir del ID pasado por Path Param. Falla si el ID no existe.'
)  # DELETE /projects
async def delete(id: Annotated[int, Path(ge=1)]) -> None:
    controller.delete(id)
