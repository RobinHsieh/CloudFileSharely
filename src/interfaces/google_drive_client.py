from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class GoogleDriveClient:
    """
    A class to interact with Google Drive API.
    Stateful class.
    Binding with Google Drive API credentials and batch requests.
    """
    def __init__(self, credentials_token):
        GoogleDriveClient.credentials = Credentials.from_authorized_user_file(
            credentials_token, 
            ['https://www.googleapis.com/auth/drive']
        )
        GoogleDriveClient.drive_service = build('drive', 'v3', credentials=GoogleDriveClient.credentials)
        self.batch_requests = None


    @staticmethod
    def callback(request_id, response, exception):
        if exception:
                # Handle error
                print(exception)
        else:
            print(f'Request_Id: {request_id}')
            print(F'Permission Id: {response.get("id")}')


    def init_start_file_batch(self):

        # Initialize batch request
        self.batch_requests = self.drive_service.new_batch_http_request(callback=GoogleDriveClient.callback)


    def append_share_file_batch(self, file_id, email_address: str, email_message: str, expiration_time: str):

        user_permission = {
            'type': 'user',
            'role': 'reader',
            "expirationTime": expiration_time,
            'emailAddress': email_address
        }
        
        self.batch_requests.add(GoogleDriveClient.drive_service.permissions().create(
            fileId=file_id,
            emailMessage=email_message,
            body=user_permission,
            fields='id',
        ))


    def execute_share_file_batch(self):
        self.batch_requests.execute()
        self.batch_requests = None
