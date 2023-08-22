from __future__ import print_function

from datetime import date, datetime, timedelta
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials

import Sharely.files_information as f_i

SCOPES = ['https://www.googleapis.com/auth/drive']


def share_file(real_file_id, real_user, offset, max_date):
    """Batch permission modification.
    Args:
        real_file_id: file Id
        real_user: User ID
        # real_domain: Domain of the user ID
        offset: How long is it from tomorrow to the day in the future
        max_date: The date when the maximum number of applications was reached
    Prints modified permissions

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    # creds, _ = google.auth.default()
    creds = Credentials.from_authorized_user_file(f_i.project_path + '/OAuth_client_ID_credentials/token.json', SCOPES)

    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)
        ids = []
        file_id = real_file_id

        def callback(request_id, response, exception):
            if exception:
                # Handle error
                print(exception)
            else:
                print(f'Request_Id: {request_id}')
                print(F'Permission Id: {response.get("id")}')
                ids.append(response.get('id'))

        # pylint: disable=maybe-no-member
        this_month = datetime.now().month
        today = datetime.now().day
        if offset == -2:
            offset = 0
        expire_date = f"{date.today()+timedelta(days=1 + offset)}T23:59:59+08:00:00"

        # Availability
        batch = service.new_batch_http_request(callback=callback)
        user_permission = {'type': 'user',
                           'role': 'reader',
                           "expirationTime": expire_date,
                           'emailAddress': real_user
                           }

        email_message = f"觀看時間至{this_month}月{today + 1 + offset}日 23:59\n\n【智慧財產權】\
        \n請本人在觀看雲端影片時，嚴禁下載、翻錄雲端影片內容，或是提供給第三人做使用。\n\n【貼心提醒】\n若覺得不清楚的話，\
        建議改用筆電或電腦(螢幕較大之設備)觀看，並且把畫質調成1080p(點選「設置」→「畫質」→「1080p」，若無自動調整請重複操作一次)，會比較清楚。\
        \n\n【問題排除】\n如遇播放影片時發生問題，請改用「無痕模式」(或「私密瀏覽」...等)試試看，如仍無法觀看請與助教聯繫。"

        if max_date != " ":
            email_message += f"\n-----------------------------------------------------------------------\n\
            提醒您：\n由於下列課程：{max_date}的申請次數已達3次，因此上述課程系統將不再自動開放，\
            若因個人原因尚有觀看需求，歡迎與助教聯絡。\n\
            -----------------------------------------------------------------------"

        email_message += "\n\n助教聯絡方式：\nEmail: hectopascal.citrus@g.ncu.edu.tw\
        \nFB: https://www.facebook.com/people/Robin-Hsieh/100004677013672/"

        # See method details in:
        # https://developers.google.com/resources/api-libraries/documentation/drive/v3/python/latest/drive_v3.permissions.html
        batch.add(service.permissions().create(fileId=file_id,
                                               emailMessage=email_message,
                                               body=user_permission,
                                               fields='id',))

        batch.execute()

    except HttpError as error:
        print(F'An error occurred: {error}')
        ids = None

    return ids
