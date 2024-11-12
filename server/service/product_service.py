#Corazon: Logica o reglas de negocio
from typing import List

from server.schemas.product_schemas import NewProductRequest, ProductResponse, ProductRequest
from server.exceptions import NotFound
from server.repository import ProductsRepository


class ProductsService:

    def __init__(self):
        self.product_repo = ProductsRepository()

    def create(self, new_product: NewProductRequest) -> ProductResponse:
        product_dict = self.product_repo.create(new_product.model_dump())
        return ProductResponse(**product_dict)

    def get_list(self, limit: int, offset: int) -> List[ProductResponse]:
        product_list = self.product_repo.get_list(limit, offset)
        # list comprenhension
        return [ProductResponse(**product)for product in product_list]

    def get_by_id(self, id: int) -> ProductResponse:
        product = self.product_repo.get_by_id(id)
        if product is None:
            raise NotFound(f'Producto con id {id} no encontrado')
        return ProductResponse(**product)

    def update(self, id: int, new_data: ProductRequest) -> ProductResponse:
        update_product = self.product_repo.update(
            id, new_data.model_dump(exclude_none=True))
        if update_product is None:
            raise NotFound(
                f'Producto con id {id} no encontrado para actualizarse')
        return ProductResponse(**update_product)

    def delete(self, id: int) -> None:
        if not self.product_repo.delete(id):
            raise NotFound(
                f'Producto con id {id} no encontrado para eliminarse')
