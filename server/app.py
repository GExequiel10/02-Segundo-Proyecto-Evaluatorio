# import logging

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from .api import api_router

# logger = logging.getLogger(__name__)
fast_products = FastAPI(title='Product Store API')

# Redirigir la raiz (/) a la documentacion (/docs)


@fast_products.get('/', include_in_schema=False)
async def root():
    return RedirectResponse(url='/docs')

# incluimos el router principal a la instancia de FastAPI
# es bueno arrancar a definir las rutas 'desde la hoja del arbol'
fast_products.include_router(api_router)


# @fast_projects.on_event('startup')
# async def startup_event():
#     logger.debug('API Iniciada')


# @fast_projects.on_event('shutdown')
# def shutdown_event():
#     logger.debug('API Finalizada')
