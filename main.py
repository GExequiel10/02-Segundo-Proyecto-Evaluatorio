import uvicorn

#esta es la forma mas prolija de definir un framework
if __name__ == '__main__':
    uvicorn.run('server.app:fast_projects',
                host='0.0.0.0', port=8000, reload=True)