from __future__ import print_function

from datetime import datetime
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials

import files_information as f_i


SCOPES = ['https://www.googleapis.com/auth/drive']


def search_file(searched_date):
    """Search file in drive location

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    # creds, _ = google.auth.default()
    creds = Credentials.from_authorized_user_file(f_i.project_path + '/token.json', SCOPES)

    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)
        files = []
        page_token = None
        while True:
            # pylint: disable=maybe-no-member
            start_date = datetime(2022, 10, 17, 0, 0, 0).isoformat() + '+08:00'
            # print(start_date)  # test
            query = f"mimeType='application/vnd.google-apps.folder' \
             and name contains '{searched_date}' and not name contains '實體課代' \
             and createdTime > '{start_date}'"

            response = service.files().list(q=query,
                                            spaces='drive',
                                            fields='nextPageToken, '
                                                   'files(id, name)',
                                            pageToken=page_token).execute()
            for file in response.get('files', []):
                # Process change
                print(F'Found file: {file.get("name")}, {file.get("id")}')
            files.extend(response.get('files', []))
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break

    except HttpError as error:
        print(F'An error occurred: {error}')
        files = None

    return files


search_file("03/22")
