from __future__ import print_function
import datetime
from logging import error
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow, Flow
from google.auth.transport.requests import Request
import os
from django.http import HttpResponseRedirect
import json

# If modifying these scopes, reset the token
SCOPES = ["https://www.googleapis.com/auth/calendar.events"]


def get_creds():
    flow = InstalledAppFlow.from_client_secrets_file("code_secret_client.json", SCOPES)
    creds = flow.run_local_server(port=8080)
    return creds


def filter_creds(creds):
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except:
                print("here i am")
                creds = get_creds()
        else:
            creds = get_creds()
    return creds


def add_event(creds, begin, end):
    """Creates an event in the Google Calendar of the user"""
    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    event = {
        "description": "an event",
        "start": {
            "dateTime": begin,
            "timeZone": "Europe/Paris",
        },
        "end": {
            "dateTime": end,
            "timeZone": "Europe/Paris",
        },
    }
    inserted_event = service.events().insert(calendarId="primary", body=event).execute()
    print("Event created: %s" % (inserted_event.get("htmlLink")))


def get_events(creds):
    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
    # TODO filter to current week
    events_result = (
        service.events()
        .list(calendarId="primary", singleEvents=True, orderBy="startTime")
        .execute()
    )
    events = events_result.get("items", [])
    return events
