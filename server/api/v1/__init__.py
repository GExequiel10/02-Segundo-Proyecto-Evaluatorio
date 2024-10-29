from fastapi import APIRouter

from .project_routes import router as project_router

# Router v1
router_v1 = APIRouter(prefix='/v1')

#Agregamos al router las rutas definidas
router_v1.include_router(project_router, tags=['Projects'])
