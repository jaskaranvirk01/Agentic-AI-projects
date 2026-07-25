from auth.google_auth import get_google_service
from langchain.tools import tool
from dateutil import parser as dtparser


@tool
def create_meeting(summary: str,
                   start_time: str,      # ISO 8601, e.g. "2026-07-28T10:00:00"
                   end_time: str,
                   timezone: str = "Asia/Kolkata",):
    """Create a Google Calendar meeting/event with the given summary, start/end time"""
    start_iso = dtparser.parse(start_time).strftime("%Y-%m-%dT%H:%M:%S")
    end_iso = dtparser.parse(end_time).strftime("%Y-%m-%dT%H:%M:%S")
    calender_service = get_google_service('calendar', 'v3')
    event = {
        'summary': summary,
        "start": {"dateTime": start_iso, "timeZone": timezone},
        "end": {"dateTime": end_iso, "timeZone": timezone},
    }
    created = calender_service.events().insert(
        calendarId='primary', body=event, sendUpdates='all'
    ).execute()

    return {"event_id": created["id"], "link": created.get("htmlLink")}
