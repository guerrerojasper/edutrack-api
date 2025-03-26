import os
import logging
from logging.handlers import RotatingFileHandler

class LogHandler(object):
    def __init__(self, logger_name, debug_mode):
        self.__identifier = logger_name
        self.__log_path = 'logs'
        self.__debug_mode = debug_mode
        self.__hadler = None
        self.__logger = None

        if self.__debug_mode:
            self.__formatter = logging.Formatter(
                '%(asctime)s | %(pathname)s:%(lineno)d | %(funcName)s | %(levelname)s | %(message)s'
            )
            self.__loglevel = logging.DEBUG
        
        else:
            self.__formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )
            self.__loglevel = logging.INFO
    
    def log_setup(self):
        # Check if logger is already initialize
        if logging.getLogger(self.__identifier).hasHandlers():
            self.__logger = logging.getLogger(self.__identifier)
            return self.__logger

        # Check path
        if self.__log_path is not None and os.path.exists(self.__log_path) is False:
            try:
                self.__log_path = os.path.join(os.getcwd(), self.__log_path)
                os.makedirs(self.__log_path)
            except Exception as e:
                print(f'Failed to create log directory. Log path: {self.__log_path}')
        
        # Configure logger
        self.__hadler = RotatingFileHandler(
            os.path.join(os.getcwd(), self.__log_path, f'{self.__identifier}.log'),
            maxBytes=1024 * 1024,
            backupCount=10
        )
        # self.__hadler.setLevel(self.__loglevel)
        self.__hadler.setFormatter(self.__formatter)

        self.__logger = logging.getLogger(self.__identifier)
        self.__logger.setLevel(self.__loglevel)
        self.__logger.addHandler(self.__hadler)
    
    def info(self, log_str):
        if self.__logger:
            self.__logger.info(f'[{self.__identifier}] {log_str}')
    
    def debug(self, log_str):
        if self.__logger:
            self.__logger.debug(f'[{self.__identifier}] {log_str}')
    
    def warning(self, log_str):
        if self.__logger:
            self.__logger.warning(f'[{self.__identifier}] {log_str}')
    
    def error(self, log_str):
        if self.__logger:
            self.__logger.error(f'[{self.__identifier}] {log_str}')
    
    def critical(self, log_str):
        if self.__logger:
            self.__logger.critical(f'[{self.__identifier}] {log_str}')
