# Archivo de barril para su facil uso con otros archivos
from .settings import Settings
from .loggins import config_logger

# aca estoy seteando una instancia de la clase Settings
# contenida en el archivo settings.
app_settings = Settings()

# aca llamamos a la funcion config_logger continada
# en el archivo loggins
config_logger (app_settings.DEBUG)