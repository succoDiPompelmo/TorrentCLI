import logging

from logging.handlers import RotatingFileHandler

def init_logger(config):
    # Add the log message handler to the logger
    # logging.basicConfig(filename='myapp.log', level=logging.DEBUG)

    logger = logging.getLogger()
    logger.setLevel(config['APP']['LOG_LEVEL'])

    rotating_log_handler = RotatingFileHandler('log/log.out', maxBytes=10000, backupCount=5)

    logger.addHandler(rotating_log_handler)