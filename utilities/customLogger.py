import logging
from selenium import webdriver

import logging

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger('demo_blaze')
        logger.setLevel(logging.INFO)
        #
        #Create file handler
        file_handler = logging.FileHandler('.\\Logs\\auto_log.log', mode='w')
        file_handler.setLevel(logging.INFO)
        #
        #Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        #Add file handler to logger
        logger.addHandler(file_handler)
        #
        return logger



