from account.user import User
from datetime import datetime

class Meeting: 
    def __init__(self, meetingId: str): 
        self._meetingId = meetingId
        self._meetingRoomId = None
        self._host = None
        self._invitees = []
        self._description = None
        self._startTime = None
        self._endTime = None

    def getMeetingId(self) -> str:
        return self._meetingId
    
    def getMeetingRoomId(self) -> str: 
        return self._meetingRoomId
    
    def getHost(self) -> User:
        return self._host
    
    def getListOfInvitees(self) -> list[User]: 
        return self._invitees
    
    def getDescription(self) -> str: 
        return self._description
    
    def setMeetingRoomId(self, meetingRoomId: str) -> "Meeting": 
        self._meetingRoomId  = meetingRoomId
        return self
    
    def setHost(self, host: User) -> "Meeting": 
        self._host = host
        return self
    
    def addInvitee(self, user: User) -> "Meeting": 
        for user_ in self._invitees:
            if user_ == user: 
                return self
        self._invitees.append(user)
        return self
    
    def setStartTime(self, startTime: datetime)->"Meeting": 
        self._startTime = startTime
        return self
    
    def setEndTime(self, endTime: datetime)->"Meeting": 
        self._endTime = endTime
        return self
    