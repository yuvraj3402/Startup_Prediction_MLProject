from project.exception import AppException
from project.logger import logging
from project.config.configuration import configuration
from project.entity.config_entity import DataValidationConfig
from project.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
import os,sys
import pandas as pd
import json



class DataValidation:
    def __init__(self,data_validation_config:DataValidationConfig,
                 data_ingestion_artifact:DataIngestionArtifact):
        try:
            logging.info(f"{'>>'*30}Data Valdaition log started.{'<<'*30} \n\n")
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise AppException(e,sys) from e




    def get_train_and_test_df(self):
        try:
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            return train_df,test_df
        except Exception as e:
            raise AppException(e,sys) from e





    def is_train_test_file_exists(self)->bool:
        try:
            logging.info("Checking if training and test file is available")
            is_train_file_exist = False
            is_test_file_exist = False

            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            is_train_file_exist = os.path.exists(train_file_path)
            is_test_file_exist = os.path.exists(test_file_path)

            is_available =  is_train_file_exist and is_test_file_exist

            logging.info(f"Is train and test file exists?-> {is_available}")
            
            if not is_available:
                training_file = self.data_ingestion_artifact.train_file_path
                testing_file = self.data_ingestion_artifact.test_file_path
                message=f"Training file: {training_file} or Testing file: {testing_file} is not present"
                raise Exception(message)

            return is_available
        except Exception as e:
            raise AppException(e,sys) from e




    def initiate_data_validation(self)->DataValidationArtifact :
        try:
            schema_file_path=self.data_validation_config.schema_file_path

            data_validation_artifact = DataValidationArtifact(schema_file_path=schema_file_path)
            return data_validation_artifact
        except Exception as e:
            raise AppException(e,sys) from e