from datetime import datetime

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from src import files_information as f_i


# 設置API憑證
SERVICE_ACCOUNT_FILE = f_i.project_path + '/token.json'
SCOPES = ['https://www.googleapis.com/auth/drive']

# Google Sheet信息
RANGE_NAME = 'A1:Z150'  # 例如：'Sheet1'

# 建立憑證
credentials = Credentials.from_authorized_user_file(
    f_i.project_path + '/OAuth_client_ID_credentials_desktop/token.json',
    SCOPES
)

# 建立Google Sheets API客戶端
sheets_service = build('sheets', 'v4', credentials=credentials)

# 獲取今日日期
today = datetime.now().strftime('%-m/%-d')


# 獲取內部的Sheet ID
def get_sheet_id(sheet_name, spreadsheet_id):
    """
    Spreadsheet: The primary object in Google Sheets. It can contain multiple Sheets
    Sheet: A single tab within a Spreadsheet

    Args:
        sheet_name (str): The name of the sheet.
        spreadsheet_id (str): The ID of the spreadsheet.
    Returns:
        int: The ID of the specified
    """
    sheets_metadata = sheets_service.spreadsheets().get(
        spreadsheetId=spreadsheet_id,
        fields='sheets(properties)'
    ).execute()

    sheets = sheets_metadata.get('sheets', '')
    sheet_id = None
    for sheet in sheets:
        if sheet['properties']['title'] == sheet_name:
            sheet_id = sheet['properties']['sheetId']
            break
    return sheet_id


# 更新Google Sheet單元格顏色
def write_cell_color(row, col, red, green, blue, spreadsheet_id, sheet_name):
    sheet_id = get_sheet_id(sheet_name, spreadsheet_id)
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
        sheets_service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()
    except HttpError as error:
        print(f"An error occurred: {error}")


# 更新Google Sheet單元格顏色(update boundary color)
def write_bulk_cells_color(row, column, row_range, red, green, blue, spreadsheet_id, sheet_name):
    """
    Guides: https://developers.google.com/sheets/api/guides/values?hl=zh-tw#python
    Args:
        row (int): The starting row index.
        col (int): The starting column index.
        row_range (int): The number of cells in a row to update.
        red (float): The red component of the color interval [0, 1].
        green (float): The green component of the color interval [0, 1].
        blue (float): The blue component of the color interval [0, 1].
        spreadsheet_id (str): The ID of the spreadsheet.
        sheet_name (str): The name of the sheet.
    """
    sheet_id = get_sheet_id(sheet_name, spreadsheet_id)

    # Prepare a list of cell values with the desired background color
    cell_values = [
        {
            "userEnteredFormat": {
                "backgroundColor": {
                    "red": red, 
                    "green": green, 
                    "blue": blue
                }
            }
        }
    ] * row_range

    # Create list containing each cells value in a row
    row_list = [{"values": cell_value} for cell_value in cell_values]

    body = {
        "requests": [
            {
                "updateCells": {
                    "rows": row_list,
                    "fields": "userEnteredFormat.backgroundColor",
                    "range": {
                        "sheetId": sheet_id,
                        "startRowIndex": row,
                        "endRowIndex": row + row_range,
                        "endRowIndex": row + row_range,
                        "startColumnIndex": column,
                        "endColumnIndex": column + 1
                    }
                }
            }
        ]
    }
    try:
        sheets_service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()
    except HttpError as error:
        print(f"An error occurred: {error}")


# 讀取單元格顏色
def get_cell_color(row, col, spreadsheet_id):
    request = sheets_service.spreadsheets().get(
        spreadsheetId=spreadsheet_id, ranges=RANGE_NAME,
        fields=
        'sheets('
            'data('
                'rowData('
                    'values('
                        'userEnteredFormat('
                            'backgroundColor'
                        ')'
                    ')'
                ')'
            ')'
        ')'
    )
    result = request.execute()

    sheet_data = result['sheets'][0]['data'][0]['rowData'][row]['values'][col]
    print("row: ", row, "col: ", col)
    print(sheet_data)
    color = sheet_data.get('userEnteredFormat', {}).get('backgroundColor', {})

    red = color.get('red', 0)
    green = color.get('green', 0)
    blue = color.get('blue', 0)

    return red, green, blue
