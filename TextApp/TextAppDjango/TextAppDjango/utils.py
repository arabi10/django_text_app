import logging
import sys


class Logging:
    logging.basicConfig(stream=sys.stdout,
                        filemode='a',
                        format='[%(asctime)s] [%(msecs)d] [%(levelname)s] %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S %z',
                        level=logging.INFO)
    @staticmethod
    def log_errors(message):
        logging.error(message)
        
    @staticmethod
    def log_info(message):
        logging.info(message)

    @staticmethod
    def log_warning(message):
        logging.warning(message)

    @staticmethod
    def flush_logs():
        sys.stdout.flush()