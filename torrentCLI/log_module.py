import logging

from logging.handlers import RotatingFileHandler

def init_logger(config, package_path):
    # Add the log message handler to the logger
    # logging.basicConfig(filename='myapp.log', level=logging.DEBUG)

    logger = logging.getLogger()
    logger.setLevel(config['APP']['LOG_LEVEL'])

    rotating_log_handler = RotatingFileHandler(str(package_path) + '/log/log.out', maxBytes=1000000, backupCount=1)

    logger.addHandler(rotating_log_handler)