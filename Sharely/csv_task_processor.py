from datetime import datetime, timedelta

from Sharely import sheet_cell_color_manager as cell_manager
from Sharely import share_file


def send_mail(data, file_ids_dic, spreadsheet_id, sheet_name):

    # Get time
    current_date_utc8 = datetime.utcnow() + timedelta(hours=8)
    this_month = current_date_utc8.month
    today = current_date_utc8.day
    today_str = str(this_month) + "/" + str(today)

    # Processing required information
    row_size = data.shape[0]
    column_size = data.shape[1]

    # Start to send email row by row
    for row in range(row_size):
        # Person's mail
        gmail = data.at[row, "電子郵件地址"]
        # How many days need to send
        file_ids = []
        offset = -2
        max_date = " "
        for column in range(5, column_size):
            date = data.iat[row, column]
            if date == today_str:
                if file_ids_dic.get(column):

                    red, green, blue = cell_manager.get_cell_color(row + 1, column, spreadsheet_id)

                    if (red, green, blue) == (1, 1, 1) or (red, green, blue) == (0, 0, 0):  # if cell's color is white
                        file_ids.append(file_ids_dic.get(column))
                        offset += 2
                        cell_manager.update_cell_color(row + 1, column, 1, 1, 0, spreadsheet_id, sheet_name)  # yellow

                    elif (red, green, blue) == (1, 1, 0):  # if cell's color is yellow
                        file_ids.append(file_ids_dic.get(column))
                        offset += 2
                        cell_manager.update_cell_color(row + 1, column, 0, 1, 0, spreadsheet_id, sheet_name)  # green

                    elif (red, green, blue) == (0, 1, 0):  # if cell's color is green
                        max_date = max_date + data.columns[column] + " "
                        file_ids.append(file_ids_dic.get(column))
                        offset += 2
                        cell_manager.update_cell_color(row + 1, column, 0, 1, 1, spreadsheet_id, sheet_name)  # blue

        if offset != -2:
            print(row, gmail)
            print(file_ids, offset)
            for file_id in file_ids:
                share_file.share_file(file_id, gmail, offset, max_date)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
