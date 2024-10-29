from typing import Annotated
from fastapi import APIRouter, Path, Query


router = APIRouter(prefix='/projects')


# seria: /projects (dentro de los estandeares rest es mejor que no termine en /)
@router.get(
    '',  # ruta
    status_code=200,
    responses={
        200: {'description': 'Listado de proyectos'},
    },
    description='Retorna una lista pagina con los proyectos. Si no hay proyectos, retorna una lista vacia.'
)  # GET /projects
async def get_list(limit: Annotated[int, Query(ge=1, le=1000)] = 10, offset: Annotated[int, Query(ge=1, le=1000)] = 0) -> list:
    return []


@router.post(
    '',  # ruta
    status_code=201,
    responses={
        201: {'description': 'Proyecto creado'},
    },
    description='Crea un proyecto nuevo pasado por Body Param. Falla si alguno de los campos obligatorios falta.'
)  # POST /projects
async def create() -> dict:
    return {}


@router.get(
    '/{id}',  # path
    status_code=200,
    responses={
        201: {'description': 'Proyecto encontrado'},
        422: {'description': 'ID no es de tipo valido. Debe ser entero'},
    },
    description='Devuelve un proyecto por ID. Falla si el ID no existe.'
)  # GET BY ID /projects
# con este Path Param valido datos en el endpoint y no en el servidor. Ahorra tiempo
async def get_by_id(id: Annotated[int, Path(ge=1)]) -> dict:
    return {'id': id}


@router.patch(
    '/{id}',  # path
    status_code=200,
    responses={
        201: {'description': 'Proyecto actualizado'},
        422: {'description': 'ID no es de tipo valido. Debe ser entero'},
    },
    description='Actualiza un proyecto con la data del Body Param. Falla si el ID no existe.'
)  # PATCH /projects
async def update(id: Annotated[int, Path(ge=1)]) -> dict:
    return {'id': id}


@router.delete(
    '/{id}',  # path
    status_code=204,
    responses={
        204: {'description': 'Proyecto borrado'},
        422: {'description': 'ID no es de tipo valido. Debe ser entero'},
    },
    description='Borra un proyecto a partir del ID pasado por Path Param. Falla si el ID no existe.'
)  # DELETE /projects
async def delete(id: Annotated[int, Path(ge=1)]) -> None:
    return None
