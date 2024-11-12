from server.external_interface import projects_api_client

class ProductsRepository:
    last_id: int = 0
    fake_db: list[dict] = []
    
    def create(self, new_product: dict) -> dict:
        from datetime import datetime
        now = datetime.now()
        ProductsRepository.last_id += 1
        new_product.update(
            id=ProductsRepository.last_id,
            created_at=now,
            update_at=now,
        )
        ProductsRepository.fake_db.append(new_product)
        return new_product

    def get_list(self, limit: int, offset: int) -> list[dict]:
        db_size = len(ProductsRepository.fake_db)
        first_index = min(db_size, offset)
        last_index = min(db_size,(first_index + limit))
        return ProductsRepository.fake_db[first_index:last_index]
        # return products_api_client.get_list(limit, offset) # ejemplo llamada a Api externa

    def get_by_id(self, id: int) -> dict | None:
        for product in ProductsRepository.fake_db:
            if product['id'] == id:
                return product

    def update(self, id: int, new_data: dict) -> dict | None:
        from datetime import datetime
        now = datetime.now()
        current_product = self.__fake_get_by_id(id) #TODO
        if current_product is None:
            return
        current_product.update(**new_data, update_at=now)
        return current_product

    def delete(self, id: int) -> bool:
        current_product = self.__fake_get_by_id(id)#TODO
        if current_product is None:
            return False
        ProductsRepository.fake_db.remove(current_product)
