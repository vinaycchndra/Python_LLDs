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
    
    def getInstance(self) -> "MeetingScheduler": 
        return self._instance

    def getAvailableMeetingRooms(startTime: datetime, endTime: datetime, capacity: int) -> list[MeetingRoom]: 
        pass 
    
    def bookMeeting(startTime: datetime, endTime: datetime, listOfUsers: list[User]) -> Meeting: 
        pass
    
    def _sendEmailToUsers(users: list[User]) -> bool: 
        pass

    def addMeetingRoom(self, meetingRoom: MeetingRoom, user: User)->bool: 
        if user.isAdmin(): 
            if meetingRoom not in self._meetingRooms: 
                self._meetingRooms.append(meetingRoom)
                return True
            print("Meeting room already exists.")
        else:
            print("you do not have permission to add meeting rooms")
        
        return False