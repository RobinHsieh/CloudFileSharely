from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os.path


# 獲取內部的Sheet ID
def get_sheet_id(sheet_name, spreadsheet_id):

    # the requested scopes of access
    scopes = ['https://www.googleapis.com/auth/drive']

    # Authenticate with the Google Sheets API using the credentials
    creds = Credentials.from_service_account_file(
        filename=os.environ["GOOGLE_APPLICATION_CREDENTIALS"],
        scopes=scopes,
    )

    # 建立Google Sheets API客戶端
    sheets_service = build('sheets', 'v4', credentials=creds)

    sheets_metadata = sheets_service.spreadsheets().get(
        spreadsheetId=spreadsheet_id, fields='sheets(properties)'
    ).execute()
    sheets = sheets_metadata.get('sheets', '')
    sheet_id = None
    for sheet in sheets:
        if sheet['properties']['title'] == sheet_name:
            sheet_id = sheet['properties']['sheetId']
            break
    return sheet_id


# 更新Google Sheet單元格顏色
def update_cell_color(row, col, red, green, blue, spreadsheet_id, sheet_name):

    # the requested scopes of access
    scopes = ['https://www.googleapis.com/auth/drive']

    # Authenticate with the Google Sheets API using the credentials
    creds = Credentials.from_service_account_file(
        filename=os.environ["GOOGLE_APPLICATION_CREDENTIALS"],
        scopes=scopes,
    )

    # 建立Google Sheets API客戶端
    sheets_service = build('sheets', 'v4', credentials=creds)

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
def update_cells_color(row, col, red, green, blue, spreadsheet_id, sheet_name):

    # the requested scopes of access
    scopes = ['https://www.googleapis.com/auth/drive']

    # Authenticate with the Google Sheets API using the credentials
    creds = Credentials.from_service_account_file(
        filename=os.environ["GOOGLE_APPLICATION_CREDENTIALS"],
        scopes=scopes,
    )

    # 建立Google Sheets API客戶端
    sheets_service = build('sheets', 'v4', credentials=creds)

    sheet_id = get_sheet_id(sheet_name, spreadsheet_id)

    # Prepare a list of cell values with the desired background color
    cell_values = [{"userEnteredFormat": {"backgroundColor": {"red": red, "green": green, "blue": blue}}}] * 150

    # Create a list of rows, each containing one cell value
    rows = [{"values": cell_value} for cell_value in cell_values]

    body = {
        "requests": [
            {
                "updateCells": {
                    "rows": rows,
                    "fields": "userEnteredFormat.backgroundColor",
                    "range": {
                        "sheetId": sheet_id,
                        "startRowIndex": row,
                        "endRowIndex": row + 150,
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


# 讀取單元格顏色
def get_cell_color(row, col, spreadsheet_id):

    # the requested scopes of access
    scopes = ['https://www.googleapis.com/auth/drive']

    # Authenticate with the Google Sheets API using the credentials
    creds = Credentials.from_service_account_file(
        filename=os.environ["GOOGLE_APPLICATION_CREDENTIALS"],
        scopes=scopes,
    )

    # 建立Google Sheets API客戶端
    sheets_service = build('sheets', 'v4', credentials=creds)

    # Google Sheet信息
    range_name = 'A1:Z150'  # 例如：'Sheet1'

    request = sheets_service.spreadsheets().get(
        spreadsheetId=spreadsheet_id, ranges=range_name,
        fields='sheets(data(rowData(values(userEnteredFormat(backgroundColor)))))'
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
