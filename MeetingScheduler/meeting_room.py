from calendar import Calendar
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
    
    def isAvailable(self,startTime: datetime, endTime: datetime) -> bool: 
        return True
