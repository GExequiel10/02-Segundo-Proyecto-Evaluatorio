
import logging
from sqlalchemy import text

from server.database import db_connection
from server.database.models import ProductModel


logger = logging.getLogger(__name__)

class ProductsRepository:
    
    def __init__(self):
        self.db = db_connection.session
    
    def create(self, new_product_dict: dict) -> dict:
        new_product = ProductModel(**new_product_dict)
        self.db.add(new_product)
        self.db.commit()
        self.db.refresh(new_product)
        return new_product.to_dict()

    def get_list(self, limit: int, offset: int, user_id: int) -> list[dict]:
        products = (self.db.query(ProductModel).order_by(text('id')).filter_by(user_id=user_id).limit(limit).offset(offset).all())
        return [product.to_dict() for product in products]
        # query = (
        #     self.db.query(ProductModel)
        #     .order_by(text('id'))
        #     .filter_by(user_id=user_id)
        #     .limit(limit)
        #     .offset(offset)
        #     )
        # logger.debug(f'Query ejecutada:{query}')
        # products = query.all()
        # return [product.to_dict() for product in products]
        
    def get_by_id(self, product_id: int) -> dict | None:
        product = self.__get_one(product_id)
        if product is None: 
            return None
        return product.to_dict()
    
    
    def update(self, id: int, new_data: dict) -> dict | None:
        product = self.__get_one(id)
        if product is None: 
            return None
        for field in new_data.keys():
            setattr(product, field, new_data[field])
        # for field, value in new_data.items():
        #     if hasattr(product, field): # para validar
        #         setattr(product, field, value)
        self.db.commit()
        self.db.refresh(product)
        return product.to_dict()

    def delete(self, id: int) -> bool:
        product = self.__get_one(id)
        if product is None: return False
        self.db.delete(product)
        self.db.commit()
        return True

    def __get_one(self, product_id:int) -> ProductModel | None:
        return self.db.query(ProductModel).filter_by(id=product_id).first()
