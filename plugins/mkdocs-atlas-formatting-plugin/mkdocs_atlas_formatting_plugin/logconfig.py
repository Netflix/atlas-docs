import logging

from .config import PLUGIN_NAME


def setup_logging(name: str, level: int = logging.INFO) -> logging:
    logger = logging.getLogger(f'{PLUGIN_NAME}.{name}')
    logger.setLevel(level)
    stream = logging.StreamHandler()
    formatter = logging.Formatter('%(levelname)-7s -  %(message)s ')
    stream.setFormatter(formatter)
    if not len(logger.handlers):
        logger.addHandler(stream)
    return logger
