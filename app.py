from src.mlprojects.logger import logging
from src.mlprojects.exception import customexception
import sys

if __name__=="__main__":
    logging.info('the execuation has started')

    try:
        a=1/0
    except Exception as e:
        logging.info('custom exception')
        raise customexception(e,sys)

