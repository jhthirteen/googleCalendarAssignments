class Assignment:
    eventSummary = ""
    dueDateStartOffset = ""
    dueDate = ""
    assignmentDescription = ""
    reminders = False

    def __init__(self, className, summary, dueDate, assignmentDescription):
        self.eventSummary = (className + " " + summary)
        self.dueDate = dueDate
        self.assignmentDescription = assignmentDescription
    
    