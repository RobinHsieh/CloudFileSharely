from datetime import datetime, timedelta

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

import src.files_information as f_i


SCOPES = ['https://www.googleapis.com/auth/drive']

creds = Credentials.from_authorized_user_file(f_i.project_path + '/OAuth_client_ID_credentials_desktop/token.json', SCOPES)

service = build('drive', 'v3', credentials=creds)

def callback(request_id, response, exception):
    if exception:
        # Handle error
        print(exception)
    else:
        print(f'Request_Id: {request_id}')
        print(F'Permission Id: {response.get("id")}')

offset = 7

current_date_utc8 = datetime.utcnow() + timedelta(hours=8)
expire_date_utc8 = current_date_utc8 + timedelta(days=offset)

batch = service.new_batch_http_request(callback=callback)


user = "robin0623.hsieh@gmail.com"

user_permission = {
    'type': 'user',
    'role': 'reader',
    "expirationTime": f"{expire_date_utc8.strftime('%Y-%m-%d')}T23:59:59+08:00:00",
    'emailAddress': user
}

email_message = f"觀看時間至{expire_date_utc8.month}月{expire_date_utc8.day}日 23:59 UTC+8\n\n【智慧財產權】\
\n請本人在觀看雲端影片時，嚴禁下載、翻錄雲端影片內容，或是提供給第三人做使用。\n\n【貼心提醒】\n若覺得不清楚的話，\
建議改用筆電或電腦(螢幕較大之設備)觀看，並且把畫質調成1080p(點選「設置」→「畫質」→「1080p」，若無自動調整請重複操作一次)，會比較清楚。\
\n\n【問題排除】\n如遇播放影片時發生問題，請改用「無痕模式」(或「私密瀏覽」...等)試試看，如仍無法觀看請與助教聯繫。"


view_limit_near_dates = " "

if view_limit_near_dates != " ":
    email_message += f"\n-----------------------------------------------------------------------\n\
    提醒您：\n由於下列課程：{view_limit_near_dates}的申請次數已達3次，因此上述課程系統將不再自動開放，\
    若因個人原因尚有觀看需求，歡迎與助教聯絡。\n\
    -----------------------------------------------------------------------"

email_message += "\n\n助教聯絡方式：\nEmail: hectopascal.citrus@g.ncu.edu.tw\
\nFB: https://www.facebook.com/people/Robin-Hsieh/100004677013672/"



batch.add(service.permissions().create(
    fileId="19l_k8kvOpWsEdBAjCt1myyknyVUcn0Su",
    emailMessage=email_message,
    body=user_permission,
    fields='id',
))

batch.add(service.permissions().create(
    fileId="1rbpiqscG8oT4OnHTBvRPJg9NyenM7tCu",
    emailMessage=email_message,
    body=user_permission,
    fields='id',
))

user = "sy24123c@gmail.com"

user_permission = {
    'type': 'user',
    'role': 'reader',
    "expirationTime": f"{expire_date_utc8.strftime('%Y-%m-%d')}T23:59:59+08:00:00",
    'emailAddress': user
}

batch.add(service.permissions().create(
    fileId="1veMPejEVepEJD5O4y4MOs7EsGPFzxFE0",
    emailMessage=email_message,
    body=user_permission,
    fields='id',
))

batch.execute()