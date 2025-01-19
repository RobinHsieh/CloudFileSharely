import json

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from src import files_information as f_i


spreadsheet_id = "1cz6I5zQtIvttM_xOOOcE4L9DtKYUq2iJRWfPh0qhN1g"
SCOPES = ['https://www.googleapis.com/auth/drive']

creds = Credentials.from_authorized_user_file(
    f_i.project_path + '/OAuth_client_ID_credentials_desktop/token.json',
    SCOPES
)
sheets_service = build('sheets', 'v4', credentials=creds)

# includeGridData=True: to get the sheet data
# includeGridData=False: to get the sheet metadata
sheets_metadata = sheets_service\
    .spreadsheets()\
    .get(spreadsheetId=spreadsheet_id, ranges=[], includeGridData=False)\
    .execute()
sheets = sheets_metadata['sheets']

# create json file and save sheets into json
with open(f_i.project_path + '/data/sheets_metadata.json', 'w') as f:
    json.dump(sheets, f, indent=4)