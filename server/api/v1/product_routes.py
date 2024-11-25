from typing import Annotated, List

from fastapi import APIRouter, Path, Query, Depends


from server.schemas.product_schemas import NewProductRequest, ProductResponse, ProductRequest
from server.controller import ProductsController
from server.exceptions import InternalServerError, NotFound
from server.schemas.auth_schemas import DecodedJwt
from server.dependencies import has_permission
from server.enums import ALL_ROLLES

router = APIRouter(prefix='/products')
router.responses = {
    500: InternalServerError.as_dict(),
}
controller = ProductsController()


@router.post(
    '',  # ruta
    status_code=201,
    responses={
        201: {'description': 'Producto creado'},
    },
    description='Crea un producto nuevo pasado por Body Param. Falla si falta alguno de los campos obligatorios.'
)  # POST /products
async def create(new_product: NewProductRequest,
                 token: DecodedJwt = Depends(has_permission(ALL_ROLLES)),
                 ) -> ProductResponse:
    return controller.create(new_product, token.user_id)


@router.get(
    '',  # ruta
    status_code=200,
    responses={
        200: {'description': 'Listado de productos'},
    },
    description='Retorna una lista paginada con los productos del negocio. Si no hay productos para mostrar, retorna una lista vacia.'
)  # GET /products
async def get_list(
    limit: Annotated[int, Query(ge=1, le=1000)] = 10,
    offset: Annotated[int, Query(ge=0)] = 0,
    token: DecodedJwt = Depends(has_permission(ALL_ROLLES)),
    ) -> List[ProductResponse]:
    return controller.get_list(limit, offset, token.user_id)


@router.get(
    '/{id}',  # path
    status_code=200,
    responses={
        201: {'description': 'Producto encontrado'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es de tipo valido. Debe ser entero'},
    },
    description='Retorna un producto por ID. Falla si el ID no existe.'
)  # GET BY ID /products/{id}
# con este Path Param valido datos en el endpoint y no en el servidor. Ahorra tiempo
async def get_by_id(
    id: Annotated[int, Path(ge=1)],
    token: DecodedJwt = Depends(has_permission(ALL_ROLLES)),
    ) -> ProductResponse:
    return controller.get_by_id(id, token)


@router.patch(
    '/{id}',  # path
    status_code=200,
    responses={
        200: {'description': 'Producto actualizado'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es de tipo valido. Debe ser entero'},
    },
    description='Actualiza un producto con la data del Body Param. Falla si el ID no existe.'
)  # PATCH /products
async def update(
    id: Annotated[int, Path(ge=1)],
    product: ProductRequest,
    token: DecodedJwt = Depends(has_permission(ALL_ROLLES)),
    ) -> ProductResponse:
    return controller.update(id, product, token)


@router.delete(
    '/{id}',  # path
    status_code=204,
    responses={
        204: {'description': 'Producto borrado'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es de tipo valido. Debe ser entero'},
    },
    description='Borra un producto a partir del ID pasado por Path Param. Falla si el ID no existe.'
)  # DELETE /products
async def delete(
    id: Annotated[int, Path(ge=1)],
    token: DecodedJwt = Depends(has_permission(ALL_ROLLES)),
    ) -> None:
    controller.delete(id, token)
