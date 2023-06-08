from Sharely import download_file, handle_csv
import pandas
from Sharely import update_cell_color as up_color
# Files information
from Sharely import files_information as f_i


print("Start----------------------------------------------------------------------------------------------------",
      handle_csv.today_str)

# Update csv files
for index, sheet_name in enumerate(f_i.spreadsheet_id_dic):
    download_file.update_file(sheet_name, f_i.spreadsheet_id_dic.get(sheet_name), f_i.SHEET_NAME_list[index])

# Access csv files
pandas.set_option("display.max_rows", 100, "display.max_columns", 20, )
data_L5 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L5.csv", sep=",")
data_L6 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L6.csv", sep=",")
data_L11 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L11.csv", sep=",")
data_L12 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L12.csv", sep=",")
data_L14 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L14.csv", sep=",")

# Update cells (fill color in sheet boundary)
up_color.update_cells_color(0, 23, 0.8, 0.8, 0.8, f_i.spreadsheet_id_dic.get("L5.csv"), f_i.SHEET_NAME_list[1])
up_color.update_cells_color(0, 23, 0.8, 0.8, 0.8, f_i.spreadsheet_id_dic.get("L6.csv"), f_i.SHEET_NAME_list[2])
up_color.update_cells_color(0, 23, 0.8, 0.8, 0.8, f_i.spreadsheet_id_dic.get("L11.csv"), f_i.SHEET_NAME_list[4])
up_color.update_cells_color(0, 15, 0.8, 0.8, 0.8, f_i.spreadsheet_id_dic.get("L12.csv"), f_i.SHEET_NAME_list[5])
up_color.update_cells_color(0, 23, 0.8, 0.8, 0.8, f_i.spreadsheet_id_dic.get("L14.csv"), f_i.SHEET_NAME_list[7])

# Send mail
handle_csv.send_mail(data_L5, f_i.L5_video_id_dic, f_i.spreadsheet_id_dic.get("L5.csv"), f_i.SHEET_NAME_list[1])
print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<|")
handle_csv.send_mail(data_L6, f_i.L6_video_id_dic, f_i.spreadsheet_id_dic.get("L6.csv"), f_i.SHEET_NAME_list[2])
print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<|")
handle_csv.send_mail(data_L11, f_i.L11_video_id_dic, f_i.spreadsheet_id_dic.get("L11.csv"), f_i.SHEET_NAME_list[4])
print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<|")
handle_csv.send_mail(data_L12, f_i.L12_video_id_dic, f_i.spreadsheet_id_dic.get("L12.csv"), f_i.SHEET_NAME_list[5])
print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<|")
handle_csv.send_mail(data_L14, f_i.L14_video_id_dic, f_i.spreadsheet_id_dic.get("L14.csv"), f_i.SHEET_NAME_list[7])

print("~End~====================================================================================================",
      handle_csv.today_str)
