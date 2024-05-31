import os
import logging
import sys
import time
from logging.handlers import TimedRotatingFileHandler

FORMATTER_STRING = "%(asctime)s — %(hostname)s — %(name)s — %(levelname)s — %(message)s"
FORMATTER = logging.Formatter(FORMATTER_STRING)
LOG_FILE = "my_app.log" # use fancy libs to make proper temp file

class HostnameFilter(logging.Filter):
        def filter(self, record):
            record.hostname = os.uname()[1]
            return True

def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addFilter(HostnameFilter())

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    logger.addHandler(console_handler)

    file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
    file_handler.setFormatter(FORMATTER)
    logger.addHandler(file_handler)

    return logger

if __name__ == "__main__":
    logger = get_logger("my_app_logger")
    logger.info("Start logging")
    logger.debug("Some debug message")
    while True:
        try:
            time.sleep(1)
            logger.info("Keep logging")
        except KeyboardInterrupt:
            logger.fatal("User get bored")
            break
