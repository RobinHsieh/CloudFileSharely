from Sharely import download_file, handle_csv
from Sharely import update_cell_color as up_color
from Sharely import files_information as f_i
from datetime import datetime, timedelta
import time


# Get time
current_date_utc8 = datetime.utcnow() + timedelta(hours=8)
this_month = current_date_utc8.month
today = current_date_utc8.day
today_str = str(this_month) + "/" + str(today)

print("Start----------------------------------------------------------------------------------------------------",
      today_str)

# Update local csv files
for index, spreadsheet_name in enumerate(f_i.spreadsheet_id_dic):
    if index in f_i.to_download:
        download_file.update_file(
            spreadsheet_name, f_i.spreadsheet_id_dic.get(spreadsheet_name), f_i.single_sheet_namelist[index]
        )

# Access csv files
pandas.set_option("display.max_rows", 150, "display.max_columns", 20, )
# 週三班
# data_L7 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L7.csv", sep=",")
# data_L8 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L8.csv", sep=",")
# data_L9 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L9.csv", sep=",")
# data_L10 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L10.csv", sep=",")
# data_L11 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L11.csv", sep=",")
data_L0 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L0.csv", sep=",")
data_L1 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L1.csv", sep=",")

# 週一班
# data_L11 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L11.csv", sep=",")

# 週二班
# data_L14 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L14.csv", sep=",")
# data_L1 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L1.csv", sep=",")
# data_L2 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L2.csv", sep=",")
# data_L3 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L3.csv", sep=",")
# data_L4 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L4.csv", sep=",")
# data_L5 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L5.csv", sep=",")
data_L6 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L6.csv", sep=",")


# Update cells (fill color in sheet boundary)
# 週三班
# up_color.update_cells_color(0, 23, 0.8, 0.8, 0.8, f_i.spreadsheet_id_dic.get("L8.csv"), f_i.single_sheet_namelist[0])
# up_color.update_cells_color(0, 23, 0.8, 0.8, 0.8, f_i.spreadsheet_id_dic.get("L9.csv"), f_i.single_sheet_namelist[0])
# up_color.update_cells_color(0, 23, 0.8, 0.8, 0.8, f_i.spreadsheet_id_dic.get("L10.csv"), f_i.single_sheet_namelist[1])
# up_color.update_cells_color(0, 23, 0.8, 0.8, 0.8, f_i.spreadsheet_id_dic.get("L11.csv"), f_i.single_sheet_namelist[0])
up_color.update_cells_color(0, 23, 0.8, 0.8, 0.8, f_i.spreadsheet_id_dic.get("L0.csv"), f_i.single_sheet_namelist[0])
up_color.update_cells_color(0, 23, 0.8, 0.8, 0.8, f_i.spreadsheet_id_dic.get("L1.csv"), f_i.single_sheet_namelist[1])

# 週一班
# up_color.update_cells_color(0, 23, 0.8, 0.8, 0.8, f_i.spreadsheet_id_dic.get("L11.csv"), f_i.single_sheet_namelist[])

# 週二班
# up_color.update_cells_color(0, 23, 0.8, 0.8, 0.8, f_i.spreadsheet_id_dic.get("L14.csv"), f_i.single_sheet_namelist[])
# up_color.update_cells_color(0, 23, 0.8, 0.8, 0.8, f_i.spreadsheet_id_dic.get("L1.csv"), f_i.single_sheet_namelist[])
# up_color.update_cells_color(0, 23, 0.8, 0.8, 0.8, f_i.spreadsheet_id_dic.get("L2.csv"), f_i.single_sheet_namelist[4])
# up_color.update_cells_color(0, 23, 0.8, 0.8, 0.8, f_i.spreadsheet_id_dic.get("L3.csv"), f_i.single_sheet_namelist[3])
# up_color.update_cells_color(0, 23, 0.8, 0.8, 0.8, f_i.spreadsheet_id_dic.get("L4.csv"), f_i.single_sheet_namelist[2])
# up_color.update_cells_color(0, 23, 0.8, 0.8, 0.8, f_i.spreadsheet_id_dic.get("L5.csv"), f_i.single_sheet_namelist[3])
up_color.update_cells_color(0, 23, 0.8, 0.8, 0.8, f_i.spreadsheet_id_dic.get("L6.csv"), f_i.single_sheet_namelist[2])


# Send mail
# print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<| L06 is below")
# handle_csv.send_mail(data_L6, f_i.L6_video_id_dic, f_i.spreadsheet_id_dic.get("L6.csv"), f_i.single_sheet_namelist[2])
# time.sleep(3)
# print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<| L08 is below")
# handle_csv.send_mail(data_L8, f_i.L8_video_id_dic, f_i.spreadsheet_id_dic.get("L8.csv"), f_i.single_sheet_namelist[0])
# print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<| L09 is below")
# handle_csv.send_mail(data_L9, f_i.L9_video_id_dic, f_i.spreadsheet_id_dic.get("L9.csv"), f_i.single_sheet_namelist[0])
# print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<| L10 is below")
# handle_csv.send_mail(data_L10, f_i.L10_video_id_dic, f_i.spreadsheet_id_dic.get("L10.csv"), f_i.single_sheet_namelist[1])
# print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<| L11 is below")
# handle_csv.send_mail(data_L11, f_i.L11_video_id_dic, f_i.spreadsheet_id_dic.get("L11.csv"), f_i.single_sheet_namelist[0])
print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<| L00 is below")
handle_csv.send_mail(data_L0, f_i.L0_video_id_dic, f_i.spreadsheet_id_dic.get("L0.csv"), f_i.single_sheet_namelist[0])
print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<| L01 is below")
handle_csv.send_mail(data_L1, f_i.L1_video_id_dic, f_i.spreadsheet_id_dic.get("L1.csv"), f_i.single_sheet_namelist[1])

# print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<| L14 is below")
# handle_csv.send_mail(data_L14, f_i.L14_video_id_dic, f_i.spreadsheet_id_dic.get("L14.csv"), f_i.single_sheet_namelist[])
# print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<| L01 is below")
# handle_csv.send_mail(data_L1, f_i.L1_video_id_dic, f_i.spreadsheet_id_dic.get("L1.csv"), f_i.single_sheet_namelist[])
time.sleep(5)
# print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<| L02 is below")
# handle_csv.send_mail(data_L2, f_i.L2_video_id_dic, f_i.spreadsheet_id_dic.get("L2.csv"), f_i.single_sheet_namelist[4])
# print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<| L03 is below")
# handle_csv.send_mail(data_L3, f_i.L3_video_id_dic, f_i.spreadsheet_id_dic.get("L3.csv"), f_i.single_sheet_namelist[3])
# print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<| L04 is below")
# handle_csv.send_mail(data_L4, f_i.L4_video_id_dic, f_i.spreadsheet_id_dic.get("L4.csv"), f_i.single_sheet_namelist[2])
# time.sleep(5)
# print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<| L05 is below")
# handle_csv.send_mail(data_L5, f_i.L5_video_id_dic, f_i.spreadsheet_id_dic.get("L5.csv"), f_i.single_sheet_namelist[3])
print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<| L06 is below")
handle_csv.send_mail(data_L6, f_i.L6_video_id_dic, f_i.spreadsheet_id_dic.get("L6.csv"), f_i.single_sheet_namelist[2])

print("~End~====================================================================================================",
      today_str)
