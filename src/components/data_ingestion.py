import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd 

from sklearn.model_selection import train_test_split
from dataclasses import dataclass  # used to create class variables.

@dataclass                         #able to define class variables directly.
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")      #data ingestion component output will be saved all the files here(in this path)
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or componenet")
        try:
            #df=pd.read_csv('notebook\data\stud.csv')
            df = pd.read_csv(r'notebook\data\stud.csv')

            logging.info("Read the datasets as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)  #train_test_split initialization

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)   #The .to_csv() method is a built-in function in Pandas that allows you to save a Pandas DataFrame as a CSV file.
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)


if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()
