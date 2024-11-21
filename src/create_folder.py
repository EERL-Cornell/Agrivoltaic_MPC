#create folders
import os

# project path 整个project folder的路径
project_path = "/Users/chenyuwang/Desktop/project/"
#folder_path
data_path = "/data/"
uncertainties_path = "/uncertainties/"
code_path = "/code/"


raw_data_path = "/data/raw_data/"
processed_data_path = "/data/processed_data/"

field_data_raw_path = "/data/raw_data/field_data_raw/"
field_data_processed_path = "/data/processed_data/field_data_processed/"

future_data_raw_path = "/data/raw_data/future_data_raw/"
future_data_processed_path = "/data/processed_data/future_data_processed/"

historical_actual_raw_path = "/data/raw_data/historical_actual_raw/"
historical_actual_processed_path = "/data/processed_data/historical_actual_processed/"

historical_forecasted_raw_path = "/data/raw_data/historical_forecasted_raw/"
historical_forecasted_processed_path = "/data/processed_data/historical_forecasted_processed/"

smpc_histogram_raw_path = "/data/raw_data/smpc_histogram_raw/"
smpc_histogram_processed_path = "/data/processed_data/smpc_histogram_processed/"

path_list = [data_path, raw_data_path, processed_data_path, 
             field_data_raw_path, field_data_processed_path, 
             future_data_raw_path, future_data_processed_path, 
             historical_actual_raw_path, historical_actual_processed_path, 
             historical_forecasted_raw_path, historical_forecasted_processed_path, 
             smpc_histogram_raw_path, smpc_histogram_processed_path,uncertainties_path,code_path]


def create_folder(project_path, path_list):
  for folder_path in path_list:
    folder_path = project_path + folder_path
    if not os.path.exists(folder_path):
      os.makedirs(folder_path)
      print(f"folder '{folder_path}' created")
    else:
      print(f"folder '{folder_path}' exist")



create_folder(project_path, path_list)