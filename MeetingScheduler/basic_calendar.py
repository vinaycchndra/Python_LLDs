from meeting import Meeting
from datetime import datetime

class Calendar: 
    def __init__(self, calendarId: str, meetingRoomId: str): 
        self._calendarId = calendarId
        self._scheduledMeetings = []
        self._meetingRoomId = meetingRoomId

    def addMeetingToCalendar(self, meeting: Meeting):
        self._scheduledMeetings.append(meeting)

    def checkAvailability(self, startTime: datetime, endTime: datetime) -> bool: 
        # Using brute force approach for looking into the overlapping intervals 
        # we check for incoming event to be non overlapping with every meeting event existing in the calendar
        for meeting in self._scheduledMeetings: 
            if  not (meeting.getStartTime() <= endTime or meeting.getEndTime() > startTime): 
                # overlapping events.
                return False
        return True