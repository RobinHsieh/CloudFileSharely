import math
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from src import files_information as f_i

SCOPES = ['https://www.googleapis.com/auth/drive']


def update_file(file_name, sheet_id):

    # Authenticate with the Google Drive API using the credentials
    creds = Credentials.from_authorized_user_file(f_i.project_path + '/token.json', SCOPES)
    drive_service = build('drive', 'v3', credentials=creds)

    # Get the file size of the Google Sheet in bytes
    file = drive_service.files().get(fileId=sheet_id,
                                     fields='id, name, mimeType, createdTime, modifiedTime, parents, size').execute()
    file_size = int(file['size'])

    # Set the maximum number of bytes to download in each request
    chunk_size = 1024 * 1024  # 1 MB

    # Set the number of chunks to download
    num_chunks = math.ceil(file_size / chunk_size)

    # Export the Google Sheet as a .csv file
    file_path = f_i.project_path + "/data/"
    mime_type = 'text/csv'
    request = drive_service.files().export_media(fileId=sheet_id, mimeType=mime_type)

    # Download the Google Sheet in chunks
    with open(file_path + file_name, 'wb') as outfile:
        for i in range(num_chunks):
            start = i * chunk_size
            end = start + chunk_size - 1
            if end > file_size:
                end = file_size - 1
            range_header = 'bytes={}-{}'.format(start, end)
            request.headers['Range'] = range_header
            chunk = request.execute()
            outfile.write(chunk)


update_file("L4.csv", f_i.spreadsheet_id_dic.get("L4.csv"))
