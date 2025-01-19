import pandas
from src import files_information as f_i

csv_data = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L1.csv", sep=",")

row_size = csv_data.shape[0]
column_size = csv_data.shape[1]

print(csv_data)
