import os
import sys # becuase we are using custom exception
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig: # whenever performing data injestion, there should be some inputs that may be probably required by data ingestion component
    # the input can be like where to save (path)the training, testing and raw data . so this inputs can be save in this class
    # In the data ingestion part, when we want any input , we can give through this class
    '''
    dataclass decorator: Inside a class, to define the class variable, we basically use init
    But we use this dataclass, we will be able to directly define our class variable
    '''
    train_data_path: str=os.path.join('artifacts',"train.csv") # data ingestion output save all the files in this path
    '''
    so this path is the input we are giving to data ingestion and later on the data ingestion will save
    train.csv in this perticular path
    '''
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()# it consist of above there path values
        '''
        so inside the ingestion_config variable we will have three sub variables -->
        train_data_path,test_data_path,raw_data_path
        '''

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion me thod or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv') # here instead of this, we can read data from DB also when we have data in the DB
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)# save stud data in raw data path directory

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )# when we pass these two, then only our next step process --> data transformation will be able to get this information
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()#initiate the class and use functions inside there
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
