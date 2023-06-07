import logging
import logging.handlers
import os.path


def check_dir(to_check_dir):
    if os.path.isdir(to_check_dir):
        print("directory bestaat")
    else:
        print("directory moet gemaakt worden")

def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    check_dir('logs')

    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')
    file_handler = logging.handlers.RotatingFileHandler('logs\healthclient.log', mode='a', maxBytes=2000000,
                                                        backupCount=10)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger
