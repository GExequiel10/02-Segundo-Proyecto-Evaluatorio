import uvicorn

from server.configs import app_settings as settings

# esta es la forma mas prolija de definir un framework
if __name__ == '__main__':
    uvicorn.run('server.app:fast_products', host='0.0.0.0', port=settings.PORT, reload=settings.DEV)
