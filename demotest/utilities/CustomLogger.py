import logging
import logging
from os import remove
from os.path import exists


class LogGen:

    # """Function returns the logger object"""
    @staticmethod
    def setup_logger(logger_name, log_file, level=logging.INFO):
        # Erase log if already exists
        if exists(log_file):
            remove(log_file)
        # Configure log file
        logger = logging.getLogger(logger_name)
        formatter = logging.Formatter('%(asctime)s :%(levelname)s: %(name)s :%(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        file_handler = logging.FileHandler(log_file, mode='w')
        file_handler.setFormatter(formatter)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.setLevel(level)
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
        return logger
