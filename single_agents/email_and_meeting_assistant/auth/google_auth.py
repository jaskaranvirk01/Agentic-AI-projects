from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build, Resource

SCOPES = [
    "https://www.googleapis.com/auth/gmail.compose",
    "https://www.googleapis.com/auth/calendar",
]

CREDENTIALS_DIR = Path('credentials')
CREDENTIALS_FILE = CREDENTIALS_DIR / 'credentials.json'
TOKEN_FILE = CREDENTIALS_DIR / 'token.json'


def get_google_service(api_name: str, api_version: str) -> Resource:
    """Return an authenticated Google API service."""

    creds = None
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            if not CREDENTIALS_FILE.exists():
                raise FileNotFoundError(
                    f"Credentials file not found: {CREDENTIALS_FILE}"
                )
            flow = InstalledAppFlow.from_client_secrets_file(
                str(CREDENTIALS_FILE), SCOPES)

            creds = flow.run_local_server(port=0)

        CREDENTIALS_DIR.mkdir(parents=True, exist_ok=True)
        TOKEN_FILE.write_text(creds.to_json())

    service = build(api_name, api_version, credentials=creds)

    return service
