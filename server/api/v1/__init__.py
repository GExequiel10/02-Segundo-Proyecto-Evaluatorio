from fastapi import APIRouter

from .product_routes import router as product_router
from .user_routes import router as user_router
from .auth_routes import router as auth_router

# Router v1
router_v1 = APIRouter(prefix='/v1')

#Agregamos al router las rutas definidas
router_v1.include_router(product_router, tags=['Products'])
router_v1.include_router(user_router, tags=['Users'])
router_v1.include_router(auth_router, tags=['Auth'])