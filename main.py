from Sharely import download_file, handle_csv
import pandas
from Sharely import update_cell_color as up_color
# Files information
from Sharely import files_information as f_i


print("Start----------------------------------------------------------------------------------------------------",
      handle_csv.today_str)

# Update csv files
for index, spreadsheet_name in enumerate(f_i.spreadsheet_id_dic):
    download_file.update_file(spreadsheet_name, f_i.spreadsheet_id_dic.get(spreadsheet_name), f_i.singleSheet_namelist[index])

# Access csv files
pandas.set_option("display.max_rows", 100, "display.max_columns", 20, )
data_L4 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L4.csv", sep=",")
data_L5 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L5.csv", sep=",")
data_L6 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L6.csv", sep=",")
data_L11 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L11.csv", sep=",")
data_L12 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L12.csv", sep=",")
data_L14 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L14.csv", sep=",")
data_L1 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L1.csv", sep=",")

# Update cells (fill color in sheet boundary)
up_color.update_cells_color(0, 23, 0.8, 0.8, 0.8, f_i.spreadsheet_id_dic.get("L4.csv"), f_i.singleSheet_namelist[0])
up_color.update_cells_color(0, 23, 0.8, 0.8, 0.8, f_i.spreadsheet_id_dic.get("L5.csv"), f_i.singleSheet_namelist[1])
up_color.update_cells_color(0, 23, 0.8, 0.8, 0.8, f_i.spreadsheet_id_dic.get("L6.csv"), f_i.singleSheet_namelist[2])
up_color.update_cells_color(0, 23, 0.8, 0.8, 0.8, f_i.spreadsheet_id_dic.get("L11.csv"), f_i.singleSheet_namelist[4])
up_color.update_cells_color(0, 15, 0.8, 0.8, 0.8, f_i.spreadsheet_id_dic.get("L12.csv"), f_i.singleSheet_namelist[5])
up_color.update_cells_color(0, 23, 0.8, 0.8, 0.8, f_i.spreadsheet_id_dic.get("L14.csv"), f_i.singleSheet_namelist[7])
up_color.update_cells_color(0, 23, 0.8, 0.8, 0.8, f_i.spreadsheet_id_dic.get("L1.csv"), f_i.singleSheet_namelist[8])

# Send mail
handle_csv.send_mail(data_L4, f_i.L4_video_id_dic, f_i.spreadsheet_id_dic.get("L4.csv"), f_i.singleSheet_namelist[0])
print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<|")
handle_csv.send_mail(data_L5, f_i.L5_video_id_dic, f_i.spreadsheet_id_dic.get("L5.csv"), f_i.singleSheet_namelist[1])
print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<|")
handle_csv.send_mail(data_L6, f_i.L6_video_id_dic, f_i.spreadsheet_id_dic.get("L6.csv"), f_i.singleSheet_namelist[2])
print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<|")
handle_csv.send_mail(data_L11, f_i.L11_video_id_dic, f_i.spreadsheet_id_dic.get("L11.csv"), f_i.singleSheet_namelist[4])
print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<|")
handle_csv.send_mail(data_L12, f_i.L12_video_id_dic, f_i.spreadsheet_id_dic.get("L12.csv"), f_i.singleSheet_namelist[5])
print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<|")
handle_csv.send_mail(data_L14, f_i.L14_video_id_dic, f_i.spreadsheet_id_dic.get("L14.csv"), f_i.singleSheet_namelist[7])
print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<|")
handle_csv.send_mail(data_L1, f_i.L1_video_id_dic, f_i.spreadsheet_id_dic.get("L1.csv"), f_i.singleSheet_namelist[8])

print("~End~====================================================================================================",
      handle_csv.today_str)
