from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class GoogleSheetClient:
    def __init__(self, credentials_file="/path/to/credentials.json"):
        # Load credentials and initialize Google Sheets API client
        self.credentials = Credentials.from_authorized_user_file(
            credentials_file, ['https://www.googleapis.com/auth/spreadsheets']
        )
        self.sheets_service = build('sheets', 'v4', credentials=self.credentials)

    def read_sheet(self, spreadsheet_id, range_name):
        """
        Reads data from a specified range in the Google Sheet.
        Args:
            spreadsheet_id (str): The ID of the spreadsheet.
            range_name (str): The range to read, e.g., 'Sheet1!A1:Z100'.
        Returns:
            list: A 2D list containing the sheet data.
        """
        try:
            result = self.sheets_service.spreadsheets().values().get(
                spreadsheetId=spreadsheet_id, range=range_name
            ).execute()
            return result.get('values', [])
        except HttpError as e:
            print(f"An error occurred while reading the sheet: {e}")
            return []

    def write_sheet(self, spreadsheet_id, range_name, values):
        """
        Writes data to a specified range in the Google Sheet.
        Args:
            spreadsheet_id (str): The ID of the spreadsheet.
            range_name (str): The range to write to, e.g., 'Sheet1!A1:Z100'.
            values (list): A 2D list of data to write.
        Returns:
            dict: The API response from Google Sheets.
        """
        try:
            body = {"values": values}
            result = self.sheets_service.spreadsheets().values().update(
                spreadsheetId=spreadsheet_id, range=range_name, valueInputOption="RAW", body=body
            ).execute()
            return result
        except HttpError as e:
            print(f"An error occurred while writing to the sheet: {e}")
            return {}

    def update_cell_format(self, spreadsheet_id, sheet_id, start_row, start_col, end_row, end_col, color):
        """
        Updates the background color of a specified cell range in the Google Sheet.
        Args:
            spreadsheet_id (str): The ID of the spreadsheet.
            sheet_id (int): The ID of the specific sheet within the spreadsheet.
            start_row (int): Starting row index (0-based).
            start_col (int): Starting column index (0-based).
            end_row (int): Ending row index (exclusive).
            end_col (int): Ending column index (exclusive).
            color (dict): RGB color values (0-1) for the background.
        Returns:
            None
        """
        try:
            body = {
                "requests": [
                    {
                        "updateCells": {
                            "rows": [
                                {
                                    "values": [
                                        {
                                            "userEnteredFormat": {
                                                "backgroundColor": color
                                            }
                                        }
                                    ]
                                }
                            ] * (end_row - start_row)
                        },
                        "fields": "userEnteredFormat.backgroundColor",
                        "range": {
                            "sheetId": sheet_id,
                            "startRowIndex": start_row,
                            "endRowIndex": end_row,
                            "startColumnIndex": start_col,
                            "endColumnIndex": end_col,
                        },
                    }
                ]
            }
            self.sheets_service.spreadsheets().batchUpdate(
                spreadsheetId=spreadsheet_id, body=body
            ).execute()
        except HttpError as e:
            print(f"An error occurred while updating cell format: {e}")

    def get_sheet_metadata(self, spreadsheet_id):
        """
        Fetches metadata for the spreadsheet, including sheet IDs and names.
        Args:
            spreadsheet_id (str): The ID of the spreadsheet.
        Returns:
            list: A list of dictionaries containing sheet names and IDs.
        """
        try:
            result = self.sheets_service.spreadsheets().get(
                spreadsheetId=spreadsheet_id
            ).execute()
            sheets = result.get('sheets', [])
            return [{"sheetId": sheet['properties']['sheetId'], "title": sheet['properties']['title']} for sheet in sheets]
        except HttpError as e:
            print(f"An error occurred while fetching sheet metadata: {e}")
            return []
