import datetime
from google.oauth2.credentials import Credentials
from googleapiclient import discovery
from googleapiclient.errors import HttpError
import files_information as f_i


# 設置API憑證
SERVICE_ACCOUNT_FILE = f_i.project_path + '/token.json'
SCOPES = ['https://www.googleapis.com/auth/drive']

# Google Sheet信息
# SPREADSHEET_ID = '1aTQe9czrAv0a7CyenfGTp7rlYLk_wx4dh05b_fsxZbE'  # L13
# SPREADSHEET_ID = '1F9HWppdZwxZ19S8gVIJVdLDJS87tFq9tnGi7R9-XApQ'  # L10
# SHEET_NAME = 'L10課後雲端'
RANGE_NAME = 'A1:Z100'  # 例如：'Sheet1'

# 建立憑證
credentials = Credentials.from_authorized_user_file(f_i.project_path + '/token.json', SCOPES)

# 建立Google Sheets API客戶端
sheets_service = discovery.build('sheets', 'v4', credentials=credentials)

# 獲取今日日期
today = datetime.datetime.now().strftime('%-m/%-d')


# 讀取Google Sheet
# def get_values_from_sheet():
#     result = sheets_service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
#     return result.get('values', [])


def get_sheet_id(sheet_name, SPREADSHEET_ID):
    sheets_metadata = sheets_service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID, fields='sheets(properties)').execute()
    sheets = sheets_metadata.get('sheets', '')
    sheet_id = None
    for sheet in sheets:
        if sheet['properties']['title'] == sheet_name:
            sheet_id = sheet['properties']['sheetId']
            break
    return sheet_id


# 更新Google Sheet單元格顏色
def update_cell_color(row, col, red, green, blue, SPREADSHEET_ID, SHEET_NAME):
    sheet_id = get_sheet_id(SHEET_NAME, SPREADSHEET_ID)
    body = {
        "requests": [
            {
                "updateCells": {
                    "rows": [
                        {
                            "values": [
                                {
                                    "userEnteredFormat": {
                                        "backgroundColor": {
                                            "red": red,
                                            "green": green,
                                            "blue": blue
                                        }
                                    }
                                }
                            ]
                        }
                    ],
                    "fields": "userEnteredFormat.backgroundColor",
                    "range": {
                        "sheetId": sheet_id,
                        "startRowIndex": row,
                        "endRowIndex": row + 1,
                        "startColumnIndex": col,
                        "endColumnIndex": col + 1
                    }
                }
            }
        ]
    }
    try:
        sheets_service.spreadsheets().batchUpdate(spreadsheetId=SPREADSHEET_ID, body=body).execute()
    except HttpError as error:
        print(f"An error occurred: {error}")


# 讀取單元格顏色
def get_cell_color(row, col, SPREADSHEET_ID):
    request = sheets_service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID, ranges=RANGE_NAME,
                                                fields='sheets(data(rowData(values(userEnteredFormat(backgroundColor)))))')
    result = request.execute()
    print(result)
    sheet_data = result['sheets'][0]['data'][0]['rowData'][row]['values'][col]
    print("row: ", row, "col: ", col)
    print(sheet_data)
    color = sheet_data.get('userEnteredFormat', {}).get('backgroundColor', {})

    red = color.get('red', 0)
    green = color.get('green', 0)
    blue = color.get('blue', 0)

    return red, green, blue


# def main():
#     values = get_values_from_sheet()
#
#     for row_idx, row in enumerate(values):
#         for col_idx, cell in enumerate(row):
#             if cell == today:
#                 red, green, blue = get_cell_color(row_idx, col_idx)
#
#                 # 根据颜色更改单元格的顏色：
#                 if (red, green, blue) == (1, 1, 1):  # 白色
#                     update_cell_color(row_idx, col_idx, 1, 1, 0)  # 更改為黃色
#                 elif (red, green, blue) == (1, 1, 0):  # 黃色
#                     update_cell_color(row_idx, col_idx, 0, 1, 0)  # 更改為綠色
#                 elif (red, green, blue) == (0, 1, 0):  # 綠色
#                     update_cell_color(row_idx, col_idx, 0, 1, 1)  # 更改為淺藍色
#
#
# if __name__ == '__main__':
#     main()
