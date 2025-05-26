# Brightspace to Google Calendar Sync Tool

### Author
Jack Hunter

## Motivation
Binghamton University uses the software D2L Brightspace to host classes. Every class hosts its assignments on the site, and there is a nice built in calendar that shows when everything is do. However, being a person who relies on Google Calendar to stay organized with my every-day life, having two important dates and deadlines cluttered across two different calendar applications was annoying, and led to me missing assignment due dates on multiple occasions. This tool automates the process of syncing data from Brightspace Classes to Google Calendar. Every "new" assignment has an automatically created and uploaded to my personal Google Calendar. 

### Future features
- [ ] Give the user the autonomy to further customize each event, with things like personal tags, reminders, etc.

### Prerequisites
* [Google Calendar API and its associated Python libraries] https://developers.google.com/workspace/calendar/api/guides/overview
* [datetime] https://docs.python.org/3/library/datetime.html
* [Internet Calendar and Scheduling for Python] https://icalendar.readthedocs.io/en/stable/

### Installing
1) Use the Python Package Manager pip to install the necessary dependencies
2) Walk through the Google Calendar API documentation (https://developers.google.com/workspace/calendar/api/quickstart/python). Pay close attention to the OAuth section, which should result in a custom, local credentials.json and token.json file that is needed to sync with your Calendar.
3) Navigate to D2L Brightspace (https://brightspace.binghamton.edu/d2l/home) and locate the "Calendar" tab.
4) Click the Subscribe Button. On the pop-up menu, select Download. You should have a feed.ics file stored locally on your machine now.
5) Ready to invoke the Program! Run the following: python3 main.py <Semester> <Year>. For example, to generate my assignments for my classes in my Spring Semester, I run: python3 main.py Spring 2025

### Built With
* [Python] https://www.python.org
