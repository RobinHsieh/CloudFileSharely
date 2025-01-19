import pandas as pd
from datetime import datetime, timezone, timedelta

from src.interfaces.google_drive_client import GoogleDriveClient
from src.interfaces.google_sheet_client import GoogleSheetClient
from src.controllers.cell_properties_manager import CellPropertiesManager


class CSVTaskProcessor:
    """
    A class to process CSV data and 
    Stateful class.
    Binding with csv data, GoogleDriveClient and GoogleSheetClient.
    """

    def __init__(self, csv_data: pd.DataFrame, file_id_dict: dict, Drive_client: GoogleDriveClient, Sheet_client: GoogleSheetClient):
        """
        Initialize the CSVTaskProcessor with a GoogleDriveClient and CellPropertiesManager.

        Args:
            csv_data (pd.DataFrame): Dataframe containing the CSV data.
            drive_client (GoogleDriveClient): Client to interact with Google Drive API.
            properties_manager (CellPropertiesManager): Manager to handle Google Sheet cell properties.
        """
        CSVTaskProcessor.current_date_utc8 = datetime.now(timezone.utc) + timedelta(hours=8)
        CSVTaskProcessor.this_month = CSVTaskProcessor.current_date_utc8.month
        CSVTaskProcessor.today = CSVTaskProcessor.current_date_utc8.day
        CSVTaskProcessor.today_str = str(CSVTaskProcessor.this_month) + "/" + str(CSVTaskProcessor.today)

        self.drive_client = Drive_client
        self.sheet_client = Sheet_client
        self.csv_data = csv_data
        self.file_id_dict = file_id_dict


    @staticmethod
    def __generate_email_message(expire_date_utc8: datetime, view_limit_near_dates: str):
        
        reminder_message = (
            f"\
            -----------------------------------------------------------------------\n\
            提醒您：\n\
            由於下列課程：{view_limit_near_dates}的申請次數已達3次，因此上述課程系統將不再自動開放，\n\
            若因個人原因尚有觀看需求，歡迎與助教聯絡。\n\
            -----------------------------------------------------------------------\n\n"
            if view_limit_near_dates.strip()  # 確認非空字串
            else ""
        )

        # f-string
        email_message = f"\
            觀看時間至 {expire_date_utc8.month}月{expire_date_utc8.day}日 23:59 UTC+8\n\n\
            【智慧財產權】\n\
            請本人在觀看雲端影片時，嚴禁下載、翻錄雲端影片內容，或是提供給第三人做使用。\n\n\
            【貼心提醒】\n\
            若覺得不清楚的話，建議改用筆電或電腦(螢幕較大之設備)觀看，並且把畫質調成1080p\n\
            (點選「設置」→「畫質」→「1080p」，若無自動調整請重複操作一次)，會比較清楚。\n\n\
            【問題排除】\n\
            如遇播放影片時發生問題，請改用「無痕模式」(或「私密瀏覽」...等)試試看，如仍無法觀看請與助教聯繫。\n\n\
            {reminder_message}\
            助教聯絡方式：\n\
            Email: hectopascal.citrus@g.ncu.edu.tw\n\
            FB: https://www.facebook.com/people/Robin-Hsieh/100004677013672/"
        
        return email_message


    def send_email_notifications(self):
        
        self.drive_client.init_start_file_batch()

        row_size = self.csv_data.shape[0]
        column_size = self.csv_data.shape[1]

        for row in range(row_size):
            self.__process_single_user_row(row, column_size)
        
        self.sheet_client.execute_write_cell_color_requests()
        self.drive_client.execute_share_file_batch()


    def __process_single_user_row(self, row, column_size):
        """
        process the data of a single user row, with each row handling one email address.
        """ 
        email_address = self.csv_data.at[row, "電子郵件地址"]
        shareable_file_id_list = []
        offset = -1
        view_limit_near_dates = " "

        for column in range(5, column_size):

            applied_date = self.csv_data.iat[row, column]
            if (applied_date != CSVTaskProcessor.today_str):
                continue

            shareable_file_id = self.file_id_dict.get(column)
            if (shareable_file_id is None):
                continue

            """
            Q: Why row + 1?
            A: Because after converting sheet into DataFrame,
                row 0 in sheet will be the column names in DataFrame.
                So, row 1 in the sheet will be row 0 in the DataFrame.
            """
            red,\
            green,\
            blue = self.sheet_client.get_cell_color(row + 1, column)

            red,\
            green,\
            blue,\
            if_view_limit_near,\
            if_view_limit_reached = CellPropertiesManager.update_cell_properties(red, green, blue)

            shareable_file_id_list,\
            offset,\
            view_limit_near_dates = CellPropertiesManager.update_gmail_user_state(
                column, 
                if_view_limit_near, 
                if_view_limit_reached, 
                self.csv_data, 
                self.file_id_dict, 
                shareable_file_id_list, 
                offset, 
                view_limit_near_dates
            )
            
            self.sheet_client.append_write_cell_color_request(row + 1, column, 1, red, green, blue)
        
        if offset > 0:
            expire_date_utc8 = CSVTaskProcessor.current_date_utc8 + timedelta(days=offset)
            expiration_time = f"{expire_date_utc8.strftime('%Y-%m-%d')}T23:59:59+08:00:00"

            email_message = CSVTaskProcessor.__generate_email_message(expire_date_utc8, view_limit_near_dates)

            for shareable_file_id in shareable_file_id_list:
                self.drive_client.append_share_file_batch(shareable_file_id, email_address, email_message, expiration_time)
            
            print("row: ", row, "email: ", email_address) # print Log
            print("shareable_file_id_list: ", shareable_file_id_list, "offset: ", offset) # print Log
            print("-----------------------------------") # print Log
