'''
Data ingestion file use to get the data from the storages,data sources,storage platform,live stream data
'''

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass  #use to create class variable 

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig


@dataclass
class DataIngestionConfig:   #----> use to save input data
    train_data_path: str=os.path.join('artifacts',"train.csv")   #tosave the ouput data in this path
    test_data_path: str=os.path.join('artifacts',"test.csv") 
    raw_data_path: str=os.path.join('artifacts',"data.csv") 
    #here we are giving the path of input data and saving the output data to the artifacts folder


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):       # to read the data from the source
        logging.info("Enter data ingestion method or components")

        try:
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info("Read the dataset as dataFrame")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
   obj=DataIngestion()
   train_data,test_data=obj.initiate_data_ingestion()

   data_transformation = DataTransformation()
   data_transformation.initiate_data_transformation(train_data,test_data)

