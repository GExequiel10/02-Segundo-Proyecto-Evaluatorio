# import logging

from fastapi import FastAPI
from fastapi.middleware import Middleware
#from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from .api import api_router
from .database import db_connection
#from .configs import api_description #TODO
from .middlewares import RequestLoggingMiddleware

api_middlewares = [
    Middleware(RequestLoggingMiddleware)
]

# logger = logging.getLogger(__name__)
fast_products = FastAPI(middleware=api_middlewares, title='Product Store API')

# Redirigir la raiz (/) a la documentacion (/docs)
@fast_products.get('/', include_in_schema=False)
async def root():
    return RedirectResponse(url='/docs')

fast_products.include_router(api_router)


@fast_products.on_event('startup')
async def startup_event():
    # if db_connection.connect():
    #     create_tables()
    db_connection.connect()
        

@fast_products.on_event('shutdown')
def shutdown_event():
    db_connection.disconnect()