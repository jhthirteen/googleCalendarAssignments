from calendarConnect import getCredentials, writeEvents
from handleICSinput import parseICS
from datetime import datetime, timezone
from pathlib import Path
import sys


def main():
    if( len(sys.argv) < 3 ):
        print("Invoke the Program with <Season> <Year> command line arguments")
        exit()

    currentTime = datetime.now(timezone.utc)

    season = sys.argv[1]
    year = sys.argv[2]

    classIdentifier = season + " " + year

    testFile = Path('/Users/jack/Desktop/feed.ics')

    assignmentList = parseICS(classIdentifier, currentTime, testFile)
    
    credentials = getCredentials()
    writeEvents(credentials, assignmentList)
    

    
main()