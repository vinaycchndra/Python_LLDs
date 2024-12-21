from basic_calendar import Calendar
from datetime import datetime

class MeetingRoom: 
    def __init__(self, meetingRoomId: str, calendar: Calendar, capacity: int): 
        self._meetingRoomId = meetingRoomId
        self._calendar = calendar
        self._capacity = capacity
    
    def getMeetingRoomId(self)-> str: 
        return self._meetingRoomId
    
    def getMeetingRoomCapacity(self) -> int: 
        return self._capacity
    
    def addMeeting(self, meeting) -> bool:
        if self._calendar.checkAvailability(startTime= meeting.getStartTime(), endTime= meeting.getEndTime()):
            self._calendar.addMeetingToCalendar(meeting)
            return True
        return False

    def isAvailable(self,startTime: datetime, endTime: datetime) -> bool: 
        return self._calendar.checkAvailability(startTime= startTime, endTime= endTime)

    def getScheduledMeetings(self):
        return self._calendar.getScheduledMeetings()