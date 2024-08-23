import os
import sys

from src.mlprojects.logger import logging
from src.mlprojects.exception import customexception
from src.mlprojects.components.data_ingestion import DataIngestion
import pandas as pd


if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    print(train_data,test_data)