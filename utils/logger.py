#it is for logging testcases executions

import logging
import os

def get_logger(name):

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
#checks logger is handles or not
    if not logger.handlers:
#if yes then it giveslog filed format
        file_handler = logging.FileHandler("logs/test_execution.log")
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s" 
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger