from datetime import datetime, timezone, timedelta

from src import sheet_cell_color_manager as cell_manager
from src import share_file


def send_mail(csv_data, file_ids_dict: dict[int, str], spreadsheet_id, sheet_name):

    # Get time
    current_date_utc8 = datetime.now(timezone.UTC) + timedelta(hours=8)

    this_month = current_date_utc8.month
    today = current_date_utc8.day
    today_str = str(this_month) + "/" + str(today)

    # Processing required information
    row_size = csv_data.shape[0]
    column_size = csv_data.shape[1]


    # Start to send email row by row
    # Each row handel one email address
    for row in range(row_size):
        # Person's mail
        gmail = csv_data.at[row, "電子郵件地址"]
        # How many days need to send
        file_ids = []
        offset = -1
        view_limit_near_dates = " "
        for column in range(5, column_size):
            date = csv_data.iat[row, column]
            if date == today_str:
                if file_ids_dict.get(column):

                    # update cell color
                    # Q: Why row + 1? 
                    # A: Because after converting sheet into DataFrame,
                    #    row 0 in sheet will be the column names in DataFrame.
                    #    So, row 1 in the sheet will be row 0 in the DataFrame.
                    red, green, blue = cell_manager.get_cell_color(row + 1, column, spreadsheet_id)

                    if (red, green, blue) == (1, 1, 1) or (red, green, blue) == (0, 0, 0):  # if cell's color is white
                        file_ids.append(file_ids_dict.get(column))
                        offset += 2
                        cell_manager.write_cell_color(row + 1, column, 1, 1, 0, spreadsheet_id, sheet_name)  # yellow

                    elif (red, green, blue) == (1, 1, 0):  # if cell's color is yellow
                        file_ids.append(file_ids_dict.get(column))
                        offset += 2
                        cell_manager.write_cell_color(row + 1, column, 0, 1, 0, spreadsheet_id, sheet_name)  # green

                    elif (red, green, blue) == (0, 1, 0):  # if cell's color is green

                        # Create a view_limit_near_dates list_string for a email(row)
                        view_limit_near_dates = view_limit_near_dates + csv_data.columns[column] + " "
                        file_ids.append(file_ids_dict.get(column))
                        offset += 2
                        cell_manager.write_cell_color(row + 1, column, 0, 1, 1, spreadsheet_id, sheet_name)  # blue

        if offset > 0:
            print(row, gmail)
            print(file_ids, offset)

            """
            TODO: create a data structure to store gmail, file_ids, offset, view_limit_near_dates, rgb
            """
            for file_id in file_ids:
                share_file.share_file(file_id, gmail, offset, view_limit_near_dates)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
