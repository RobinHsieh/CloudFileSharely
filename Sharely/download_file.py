import csv
import os.path
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from Sharely import files_information as f_i


def update_file(spreadsheet_name, spreadsheet_id, single_sheet_name):

    # the requested scopes of access
    scopes = ['https://www.googleapis.com/auth/drive']

    # Authenticate with the Google Sheets API using the credentials
    creds = Credentials.from_service_account_file(
        filename=os.environ["GOOGLE_APPLICATION_CREDENTIALS"],
        scopes=scopes,
    )

    sheets_service = build('sheets', 'v4', credentials=creds)

    # Get the sheet ID of the specified sheet name
    sheets_metadata = sheets_service.spreadsheets().get(
        spreadsheetId=spreadsheet_id, ranges=[], includeGridData=False
    ).execute()
    sheets = sheets_metadata['sheets']

    sheet_id = None
    for sheet in sheets:
        if sheet['properties']['title'] == single_sheet_name:
            sheet_id = sheet['properties']['sheetId']
            break

    if sheet_id is None:
        raise ValueError("Sheet with name '{}' not found in the spreadsheet.".format(single_sheet_name))

    # Get the data from the specified sheet
    range_name = single_sheet_name
    result = sheets_service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    rows = result.get('values', [])

    # Write the data to a CSV file
    file_path = f_i.project_path + "/data/"
    with open(file_path + spreadsheet_name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)
