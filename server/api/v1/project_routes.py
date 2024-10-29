from fastapi import APIRouter

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
async def get_list() -> list:
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
async def get_by_id(id: int) -> dict:
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
async def update(id: int) -> dict:
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
async def delete(id: int) -> None:
    return None
