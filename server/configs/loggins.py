import os
import logging
from logging.handlers import TimedRotatingFileHandler


def config_logger(debug_level: bool):
    LOGS_PATCH = './logs'
    if not os.path.exists(LOGS_PATCH):
        os.makedirs(LOGS_PATCH)

    log_filename = LOGS_PATCH + '/fast-product'
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG if debug_level else logging.INFO)

    handler = TimedRotatingFileHandler(
        log_filename,
        when='midnight',
        interval=1,
        backupCount=0,
    )

    handler.suffix = '.log%Y%m%d'  # fast-product.log20241025

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y%m%d %H:%M:%S'
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)
