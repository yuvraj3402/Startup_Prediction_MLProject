from project.logger import logging
from project.exception import AppException
from project.entity.config_entity import DataIngestionConfig
from project.entity.artifact_entity import DataIngestionArtifact
import pandas as pd
import numpy as np
import os,sys
from sklearn.model_selection import train_test_split


class DataIngestion:


    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'>>'*20}Data Ingestion log started.{'<<'*20} ")
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise AppException(e,sys) from e
        
        


    def split_data_as_train_test(self)-> DataIngestionArtifact:
        try:
            project_file_name="startup.csv"
            data_frame=pd.read_csv(self.data_ingestion_config.dataset_url)


            train, test = train_test_split(data_frame, test_size=0.2,random_state=53)
  


            train_file_path=os.path.join(self.data_ingestion_config.ingested_train_dir,project_file_name)
            test_file_path=os.path.join(self.data_ingestion_config.ingested_test_dir,project_file_name)

            if train is not None:
                os.makedirs(self.data_ingestion_config.ingested_train_dir,exist_ok=True)
                train.to_csv(train_file_path,index=False)

                os.makedirs(self.data_ingestion_config.ingested_test_dir,exist_ok=True)
                test.to_csv(test_file_path,index=False)

                data_ingestion_artifact=DataIngestionArtifact(train_file_path=train_file_path,
                                                              test_file_path=test_file_path)
                
                return data_ingestion_artifact
        except Exception as e:
            raise AppException(e,sys) from e
        


    def initiate_data_ingestion(self):
        try:
            return self.split_data_as_train_test()
        except Exception as e:
            raise AppException(os,sys) from e