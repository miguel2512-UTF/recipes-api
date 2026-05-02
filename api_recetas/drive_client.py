import io

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaIoBaseUpload
import os
import json

credentials = json.loads(os.getenv("SERVICE_ACCOUNT"))

credentials = service_account.Credentials.from_service_account_info(
    credentials,
    scopes = ["https://www.googleapis.com/auth/drive"]
)
service_client = build("drive", "v3", credentials=credentials)

def create_file(file, file_name, folder_id):
    media = MediaIoBaseUpload(
        file.file,
        mimetype=file.content_type,
        resumable=True
    )

    file_metadata = {
        "name": file_name,
        "parents": [folder_id]
    }

    file = service_client.files().create(
        body=file_metadata,
        media_body=media
    ).execute()

    print(file)

    return file.get("id")

def update_file(file_id, file):
    media = MediaIoBaseUpload(
        file.file,
        mimetype=file.content_type,
        resumable=True
    )

    service_client.files().update(
        fileId=file_id,
        media_body=media,
    ).execute()

def delete_file(file_id):
    service_client.files().delete(fileId=file_id).execute()
    
def get_media_file(file_id):
    request_drive = service_client.files().get_media(fileId=file_id)
    buffer = io.BytesIO()
    downloader = MediaIoBaseDownload(buffer, request_drive)
    done = False

    while not done:
        status, done = downloader.next_chunk()
        print(f"Download {int(status.progress() * 100)}.")

    buffer.seek(0)

    return buffer