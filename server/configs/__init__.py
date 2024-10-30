from .settings import Settings
from .loggins import config_logger

app_settings = Settings()
config_logger (app_settings.DEBUG)