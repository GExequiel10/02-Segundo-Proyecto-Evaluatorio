from fastapi import FastAPI

from .api import api_router

fast_projects = FastAPI()

# incluimos el router principal a la instancia de FastAPI
# es bueno arrancar a definir las rutas 'desde la hoja del arbol'
fast_projects.include_router(api_router)
