import icalendar
from assignment import Assignment

#NOTE: classname is filtered within the LOCATION field
# how does Binghamton schedule their class assignments? 
# bits 0-10 of the location string should be Spring 2025
# command line argument? (Season) (Year) for semestar parsing
#NOTE: due date times are stored in UTC --> does this automatically adjust to local time when creating an event using Google Calendar? 

def parseICS(classIdentifier, currentTime, icsFile):
    calendarParser = icalendar.Calendar.from_ical(icsFile.read_bytes())

    validAssignments = []

    for event in calendarParser.events:
        if( event.get("LOCATION")[0:len(classIdentifier)] == classIdentifier ):
            dueDate = event.get("DTEND").dt
            if( dueDate > currentTime ):
                classNameEndIndex = event.get("LOCATION").rfind('(')
                className = event.get("LOCATION")[len(classIdentifier)+1:classNameEndIndex-1]
                assignmentName = event.get("SUMMARY")
                description = event.get("DESCRIPTION")
                dueDate = event.get("DTEND").dt
                validAssignments.append(Assignment(className, assignmentName, dueDate, description))
    
    return validAssignments