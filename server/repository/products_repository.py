from server.database import db_connection
from server.database.models import ProductModel


class ProductsRepository:
    
    def __init__(self):
        self.db = db_connection.session
    
    def create(self, new_product_dict: dict) -> dict:
        new_product = ProductModel(**new_product_dict)
        self.db.add(new_product)
        self.db.commit()
        self.db.refresh(new_product)
        return self.__to_dict(new_product)

    def get_list(self, limit: int, offset: int) -> list[dict]:
        products = self.db.query(ProductModel).order_by('id').limit(limit).offset(offset).all()
        return [self.__to_dict(product) for product in products]
        
    def get_by_id(self, product_id: int) -> dict | None:
        product = self.__get_one(product_id)
        if product is None: return
        return self.__to_dict(product)

    def update(self, id: int, new_data: dict) -> dict | None:
        product = self.__get_one(id)
        if product is None: return
        for field in new_data.keys():
            setattr(product, field, new_data[field])
        self.db.commit()
        self.db.refresh(product)
        return self.__to_dict(product)

    def delete(self, id: int) -> bool:
        product = self.__get_one(id)
        if product is None: return False
        self.db.delete(product)
        self.db.commit()
        return True

    def __get_one(self, product_id:int) -> ProductModel | None:
        return self.db.query(ProductModel).filter_by(id=product_id).first()

    def __to_dict(self, product: ProductModel) -> dict:
        return{
            column.name: getattr(product, column.name)
            for column in ProductModel.__table__.columns
        }