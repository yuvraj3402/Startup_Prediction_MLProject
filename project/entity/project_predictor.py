from project.exception import AppException
import os,sys
import pandas as pd
from project.util import load_object




class projectData:

    def __init__(self,
                 RD_Spend: float,
                 Administration: float,
                 Marketing_Spend: float,
                 State: str,
                 Profit: float = None):
        try:
            self.RD_Spend =  RD_Spend
            self.Administration = Administration
            self.Marketing_Spend = Marketing_Spend
            self.State = State
            self.Profit = Profit
        except Exception as e:
            raise AppException(e,sys) from e
        


    def get_project_data_as_dict(self):
        try:
            input_data={"R&D Spend":[self.RD_Spend],
                        "Administration":[self.Administration],
                        "Marketing Spend":[self.Marketing_Spend],
                        "State":[self.State]
            }

            return input_data
        except Exception as e:
            raise AppException(e,sys) from e
        

    def get_project_dataframe(self):
        try:
            input_data=self.get_project_data_as_dict()

            return pd.DataFrame(input_data)
        except Exception as e:
            raise AppException(e,sys) from e
        


class projectPredictor:

    def __init__(self,model_dir):
        try:
            self.model_dir=model_dir
        except Exception as e:
            raise AppException(e,sys) from e


    def get_latest_model_path(self):
        try:
            folder_name=list(map(int, os.listdir(self.model_dir)))
            latest_model_dir=os.path.join(self.model_dir,f"{max(folder_name)}")
            file_name=os.listdir(latest_model_dir)[0]
            latest_model_path = os.path.join(latest_model_dir, file_name)
            return latest_model_path
        except Exception as e:
            raise AppException(e,sys) from e
        
    def predict(self,X):
        try:
            model_path=self.get_latest_model_path()
            model=load_object(file_path=model_path)
            profit=model.predict(X)
            return profit
        except Exception as e:
            raise AppException(e,sys) from e
