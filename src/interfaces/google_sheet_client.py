# -*- coding: utf-8 -*-
import csv

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class GoogleSheetClient:
    """
    A class to interact with Google Sheets API.
    Stateful class.
    Binding with Google Sheets API credentials, requests and sheet.
    Guides: https://developers.google.com/sheets/api/reference/rest
    """
    def __init__(self, spreadsheet_id, sheet_name, credentials_token):
        """
        Args:
            spreadsheet_id (str): The ID of the spreadsheet.
            sheet_name (str): The name of the sheet to fetch.
            credentials_token (str): The path to the credentials token file.
        """
        self.spreadsheet_id = spreadsheet_id
        self.sheet_name = sheet_name

        # Load credentials and initialize Google Sheets API client
        GoogleSheetClient.credentials = Credentials.from_authorized_user_file(
            credentials_token, ['https://www.googleapis.com/auth/drive']
        )
        GoogleSheetClient.sheets_service = build('sheets', 'v4', credentials=GoogleSheetClient.credentials)

        self.write_cell_color_requests_list = []


    def get_sheet_as_csv(self, spreadsheet_name, file_path):
        """
        Fetches the data from a Google Sheet and writes it to a CSV file.
        Guides: https://developers.google.com/sheets/api/guides/values?hl=zh-tw#python
        Guides: https://developers.google.com/sheets/api/guides/values#read
        Args:
            spreadsheet_name (str): The name of the CSV file to write.
            file_path (str): The path to the directory where the CSV file will be written.
        """

        # Get the data from the specified sheet
        result = (GoogleSheetClient.sheets_service.spreadsheets()
            .values()
            .get(spreadsheetId=self.spreadsheet_id, range=self.sheet_name)
            .execute()
        )
        rows = result.get('values', [])

        # Write the data to a CSV file
        with open(file_path + spreadsheet_name, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows)


    def __get_sheet_id(self):
        """
        Fetches the ID of a specific sheet within a spreadsheet.
        Args:
            sheet_name (str): The name of the sheet.
            spreadsheet_id (str): The ID of the spreadsheet.
        Returns:
            int: The ID of the sheet.
        """

        sheets_metadata = GoogleSheetClient.sheets_service.spreadsheets().get(
            spreadsheetId=self.spreadsheet_id,
            fields='sheets(properties)'
        ).execute()

        sheets = sheets_metadata.get('sheets', '')
        sheet_id = None
        for sheet in sheets:
            if sheet['properties']['title'] == self.sheet_name:
                sheet_id = sheet['properties']['sheetId']
                break
        return sheet_id


    def append_write_cell_color_request(self, row, column, row_range, red, green, blue):
        """
        Updates the background color of a range of cells in a Google Sheet.
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
        sheet_id = self.__get_sheet_id()

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

        requests = {
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
        self.write_cell_color_requests_list.append(requests)


    def execute_write_cell_color_requests(self):
        """
        Executes a batch of write cell format requests.
        """
        body = {
            "requests": self.write_cell_color_requests_list
        }
        try:
            GoogleSheetClient.sheets_service.spreadsheets().batchUpdate(spreadsheetId=self.spreadsheet_id, body=body).execute()
        except HttpError as error:
            print(f"An error occurred: {error}")


    def get_cell_color(self, row, column):
        request = GoogleSheetClient.sheets_service.spreadsheets().get(
            spreadsheetId=self.spreadsheet_id, 
            ranges=self.sheet_name,
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

        sheet_data = result['sheets'][0]['data'][0]['rowData'][row]['values'][column]
        # print("row: ", row, "col: ", col)
        # print(sheet_data)
        color = sheet_data.get('userEnteredFormat', {}).get('backgroundColor', {})

        red = color.get('red', 0)
        green = color.get('green', 0)
        blue = color.get('blue', 0)

        return red, green, blue