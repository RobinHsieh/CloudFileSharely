import pandas as pd
from datetime import datetime, timedelta, timezone

from src.interfaces import google_drive_client as drive_client
from src.interfaces import google_sheet_client as sheet_client
from src.controllers import cell_properties_manager as cell_manager
from src.controllers import csv_task_processor as csv_processor
from src import files_information as f_i


# Get time
current_date_utc8 = datetime.now(timezone.utc) + timedelta(hours=8)
this_month = current_date_utc8.month
today = current_date_utc8.day
today_str = str(this_month) + "/" + str(today)

print("Start----------------------------------------------------------------------------------------------------",
      today_str)

# L0_sheet_client = sheet_client.GoogleSheetClient(f_i.spreadsheet_id_dict.get("L0.csv"), f_i.sheet_name_list[0], f_i.project_path + '/OAuth_client_ID_credentials_desktop/token.json')
# L1_sheet_client = sheet_client.GoogleSheetClient(f_i.spreadsheet_id_dict.get("L1.csv"), f_i.sheet_name_list[1], f_i.project_path + '/OAuth_client_ID_credentials_desktop/token.json')
L2_sheet_client = sheet_client.GoogleSheetClient(f_i.spreadsheet_id_dict.get("L2.csv"), f_i.sheet_name_list[2], f_i.project_path + '/OAuth_client_ID_credentials_desktop/token.json')
# L6_sheet_client = sheet_client.GoogleSheetClient(f_i.spreadsheet_id_dict.get("L6.csv"), f_i.sheet_name_list[3], f_i.project_path + '/OAuth_client_ID_credentials_desktop/token.json')

# L0_sheet_client.get_sheet_as_csv("L0.csv", f_i.project_path + "/data/")
# L1_sheet_client.get_sheet_as_csv("L1.csv", f_i.project_path + "/data/")
L2_sheet_client.get_sheet_as_csv("L2.csv", f_i.project_path + "/data/")
# L6_sheet_client.get_sheet_as_csv("L6.csv", f_i.project_path + "/data/")

# data_L0 = pd.read_csv(filepath_or_buffer=f_i.project_path + "/data/L0.csv", sep=",")
# data_L1 = pd.read_csv(filepath_or_buffer=f_i.project_path + "/data/L1.csv", sep=",")
data_L2 = pd.read_csv(filepath_or_buffer=f_i.project_path + "/data/L2.csv", sep=",", skip_blank_lines=False) # Debugging
# data_L6 = pd.read_csv(filepath_or_buffer=f_i.project_path + "/data/L6.csv", sep=",")

# L0_sheet_client.append_write_cell_color_request(0, 23, data_L0.shape[0], 0.8, 0.8, 0.8)
# L1_sheet_client.append_write_cell_color_request(0, 23, data_L1.shape[0], 0.8, 0.8, 0.8)
# print(data_L2.shape[0]) # Debugging
L2_sheet_client.append_write_cell_color_request(0, 23, data_L2.shape[0]+1, 0.8, 0.8, 0.8)
L2_sheet_client.execute_write_cell_color_requests()
# L6_sheet_client.append_write_cell_color_request(0, 23, data_L6.shape[0], 0.8, 0.8, 0.8)

Drive_client = drive_client.GoogleDriveClient(f_i.project_path + '/OAuth_client_ID_credentials_desktop/token.json')

# L0_csv_processor = csv_processor.CSVTaskProcessor(data_L0, f_i.L0_video_id_dict, Drive_client, L0_sheet_client)
# L1_csv_processor = csv_processor.CSVTaskProcessor(data_L1, f_i.L1_video_id_dict, Drive_client, L1_sheet_client)
print("@.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o< @.@ *_* >o<| L2 is below")
L2_csv_processor = csv_processor.CSVTaskProcessor(data_L2, f_i.L2_video_id_dict, Drive_client, L2_sheet_client)
# L6_csv_processor = csv_processor.CSVTaskProcessor(data_L6, f_i.L6_video_id_dict, Drive_client, L6_sheet_client)

# L0_csv_processor.send_email_notifications()
# L1_csv_processor.send_email_notifications()
L2_csv_processor.send_email_notifications()
# L6_csv_processor.send_email_notifications()


print("End------------------------------------------------------------------------------------------------------",
      today_str)