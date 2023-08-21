from __future__ import print_function

import os.path

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']


def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """

    # 使用服務帳戶憑證
    creds = Credentials.from_service_account_file(
        os.path.join(os.environ['GITHUB_WORKSPACE'], 'Service_account_credentials', 'credentials.json'),
        scopes=SCOPES
    )

    # creds = Credentials.from_service_account_file(
    #     filename=os.environ["GOOGLE_APPLICATION_CREDENTIALS"],
    #     scopes=SCOPES,
    # )

    try:
        service = build('drive', 'v3', credentials=creds)

        # Call the Drive v3 API
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
            return
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()