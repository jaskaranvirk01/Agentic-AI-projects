from langchain.tools import tool
import base64
from email.mime.text import MIMEText
from auth.google_auth import get_google_service


@tool
def create_gmail_draft(to: str, subject: str, body: str) -> str:
    """
    Create a draft email in the authenticated user's Gmail account.

    Use this tool whenever the user asks to draft an email.
    """

    gmail_service = get_google_service("gmail", "v1")

    message = MIMEText(body)
    message["To"] = to
    message["Subject"] = subject

    encoded_message = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    draft = {
        "message": {
            "raw": encoded_message
        }
    }

    created_draft = (
        gmail_service.users()
        .drafts()
        .create(
            userId="me",
            body=draft
        )
        .execute()
    )

    return f"Draft created successfully. Draft ID: {created_draft['id']}"
