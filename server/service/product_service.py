from typing import List

from server.schemas.product_schemas import NewProductRequest, ProductResponse, ProductRequest
from server.exceptions import NotFound
from server.repository import ProductsRepository


class ProductsService:

    def __init__(self):
        self.product_repo = ProductsRepository()

    def create(self, new_product: NewProductRequest, user_id:int) -> ProductResponse:
        new_product_dict = new_product.model_dump()
        new_product_dict.update(user_id=user_id)
        product_dict = self.product_repo.create(new_product_dict)
        return ProductResponse(**product_dict)

    def get_list(self, limit: int, offset: int, user_id:int) -> List[ProductResponse]:
        product_list = self.product_repo.get_list(limit, offset, user_id)
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
                f'Producto con id {id} no encontrado para actualizarlo')
        return ProductResponse(**update_product)

    def delete(self, id: int) -> None:
        if not self.product_repo.delete(id):
            raise NotFound(
                f'Producto con id {id} no encontrado para eliminar')
