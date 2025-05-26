import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]

def getCredentials():
  creds = None
  # checks if we have a token.json (to store user credentials) --> automatically created at the end of the O-auth flow
  if( os.path.exists("token.json") ):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # if there are not valid credentials --> let the user log in
    if( (not creds) or (not creds.valid) ):
      if( (creds) and (creds.expired) and (creds.refresh_token) ):
        creds.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)
      # Save the credentials for the next run
      with open("token.json", "w") as token:
        token.write(creds.to_json())
    
    return creds

def writeEvents(creds, assignmentsToAdd):
  for assignment in assignmentsToAdd:
    try:
      service = build("calendar", "v3", credentials=creds)
      now = datetime.datetime.now(tz=datetime.timezone.utc).isoformat()
      # find the minimum and maximum bounds to search for events over --> optimizes response time 
      # .isoformat() maps directly to the FRC 3339 format which is needed for Google Calendar API requests
      minBound = assignmentsToAdd[0].dueDate.isoformat()
      maxBound = assignmentsToAdd[-1].dueDate.isoformat()

      events_result = (
          service.events()
          .list(
              calendarId="primary",
              timeMin=minBound,
              timeMax=maxBound,
              q=assignment.eventSummary
          )
          .execute()
      )
      events = events_result.get("items", [])
      # if the event does not exist --> then we can add it to the calendar. Otherwise, the assignment has already been added and we should move on 
      if( events == [] ):
        eventAdd = {
          'summary': assignment.eventSummary,
          'description': assignment.assignmentDescription,
          'start': {
            'dateTime': assignment.dueDate.isoformat(),
            'timeZone': 'America/New_York',
          },
          'end': {
            'dateTime': assignment.dueDate.isoformat(),
            'timeZone': 'America/New_York',
          },
        }
        eventAdd = service.events().insert(calendarId='primary', body=eventAdd).execute()
        print(assignment.eventSummary + " added to the calendar")

    except HttpError as error:
      print(f"An error occured: {error}")