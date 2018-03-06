import datetime

i = datetime.datetime.now()

class DateCount:
    """This program calculates the days 
    until certain event."""

    def __init__(self, event, dateofevent):
        self.eventname = event
        self.eventtime = dateofevent

    def numberofdays(self):
        today = datetime.date(i.year, i.month, i.day)
        yyyy = int(self.eventtime[0:4])
        mm = int(self.eventtime[4:6])
        dd = int(self.eventtime[6:8])
        eventdate = datetime.date(yyyy, mm, dd)
        numberofdays = (eventdate - today).days
        return int(numberofdays)

event = DateCount("Graduation", "20180512")
print("My" , event.eventname , "is in" , event.numberofdays() , "days!")