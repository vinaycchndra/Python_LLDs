from account.user import User
from meeting_room import MeetingRoom
from meeting import Meeting
from datetime import datetime

class MeetingScheduler: 
    _instance = None
    
    def __new__(cls, *args, **kwargs): 
        if cls._instance is None: 
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self): 
        self._meetingRooms = []
    
    def getAvailableMeetingRooms(startTime: datetime, endTime: datetime, capacity: int) -> list[MeetingRoom]: 
        pass 
    
    def bookMeeting(startTime: datetime, endTime: datetime, listOfUsers: list[User]) -> Meeting: 
        pass
    
    def _sendEmailToUsers(users: list[User]) -> bool: 
        pass