from typing import List

from server.schemas.user_schemas import NewUserRequest, UserResponse, UserRequest
from server.exceptions import NotFound
from server.repository import ProductsRepository


class ProductsService:

    def __init__(self):
        self.product_repo = ProductsRepository()

    def create(self, new_product: NewUserRequest) -> UserResponse:
        product_dict = self.product_repo.create(new_product.model_dump())
        return UserResponse(**product_dict)

    def get_list(self, limit: int, offset: int) -> List[UserResponse]:
        product_list = self.product_repo.get_list(limit, offset)
        # list comprenhension
        return [UserResponse(**product)for product in product_list]

    def get_by_id(self, id: int) -> UserResponse:
        product = self.product_repo.get_by_id(id)
        if product is None:
            raise NotFound(f'Producto con id {id} no encontrado')
        return UserResponse(**product)

    def update(self, id: int, new_data: UserRequest) -> UserResponse:
        update_product = self.product_repo.update(
            id, new_data.model_dump(exclude_none=True))
        if update_product is None:
            raise NotFound(
                f'Producto con id {id} no encontrado para actualizarse')
        return UserResponse(**update_product)

    def delete(self, id: int) -> None:
        if not self.product_repo.delete(id):
            raise NotFound(
                f'Producto con id {id} no encontrado para eliminarse')
