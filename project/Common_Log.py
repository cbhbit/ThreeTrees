import logging
import logging.config


class CommonLog:
    log_filename = "logging.log"

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG,
                            format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            filemode='a')
    def append(self,s):
        pass