
import tempfile

from googleapiclient.http import MediaIoBaseDownload
from langchain_google_community import GoogleDriveLoader
from langchain_community.document_loaders import PyPDFLoader
from googleapiclient.discovery import build


class GoogleDrivePDFLoader(GoogleDriveLoader):
    def _load_file_from_id(self, file_id):
        creds = self._load_credentials()
        service = build("drive", "v3", credentials=creds)

        request = service.files().get_media(fileId=file_id)
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")

        downloader = MediaIoBaseDownload(tmp, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()

        tmp.close()

        loader = PyPDFLoader(tmp.name)
        return loader.load()
