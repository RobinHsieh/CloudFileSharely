import download_file
import handle_csv
import pandas
# Files information
import files_information as f_i


print("Start----------------------------------------------------------------------------------------------------")
# Update csv files
for file_name in f_i.file_dic:
    download_file.update_file(file_name, f_i.file_dic.get(file_name))

# Access csv files
pandas.set_option("display.max_rows", 100, "display.max_columns", 20, )
data_L4 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L4.csv", sep=",")
data_L5 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L5.csv", sep=",")
data_L10 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L10.csv", sep=",")
data_L11 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L11.csv", sep=",")
data_L13 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L13.csv", sep=",")
data_L14 = pandas.read_csv(filepath_or_buffer=f_i.project_path + "/data/L14.csv", sep=",")

# Send mail
handle_csv.send_mail(data_L4, f_i.L4_file_id_dic, f_i.L4_SPREADSHEET_ID, f_i.L4_SHEET_NAME)
handle_csv.send_mail(data_L5, f_i.L5_file_id_dic, f_i.L5_SPREADSHEET_ID, f_i.L5_SHEET_NAME)
handle_csv.send_mail(data_L10, f_i.L10_file_id_dic, f_i.L10_SPREADSHEET_ID, f_i.L10_SHEET_NAME)
handle_csv.send_mail(data_L11, f_i.L11_file_id_dic, f_i.L11_SPREADSHEET_ID, f_i.L11_SHEET_NAME)
handle_csv.send_mail(data_L13, f_i.L13_file_id_dic, f_i.L13_SPREADSHEET_ID, f_i.L13_SHEET_NAME)
handle_csv.send_mail(data_L14, f_i.L14_file_id_dic, f_i.L14_SPREADSHEET_ID, f_i.L14_SHEET_NAME)
print("~End~====================================================================================================")
