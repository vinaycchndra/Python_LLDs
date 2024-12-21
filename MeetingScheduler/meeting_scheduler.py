from account.user import User
from meeting_room import MeetingRoom
from meeting import Meeting
from datetime import datetime
from email_service import EmailService
from uuid import uuid4

class MeetingScheduler: 
    _instance = None
    
    def __new__(cls, *args, **kwargs): 
        if cls._instance is None: 
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self): 
        self._meetingRooms = []
        self._mailService = EmailService()
    @classmethod
    def getInstance(cls) -> "MeetingScheduler": 
        return cls._instance

    def getAvailableMeetingRooms(self, startTime: datetime, endTime: datetime, capacity: int) -> list[MeetingRoom]: 
        available_meeting_rooms = []
        for meeting_room in self._meetingRooms:
            if meeting_room.getMeetingRoomCapacity() >= capacity and meeting_room.isAvailable(startTime = startTime, endTime = endTime):
                available_meeting_rooms.append(meeting_room)
        return available_meeting_rooms
    
    def bookMeeting(self, host: User, meetingRoom: MeetingRoom, startTime: datetime, endTime: datetime, description: str, listOfUsers: list[User]) -> Meeting: 
        meeting = Meeting(meetingId= uuid4())
        if meetingRoom.getMeetingRoomCapacity() < listOfUsers.__len__(): 
            raise Exception(f"Meeting room can not hold {listOfUsers.__len__()} people")
        
        meeting.setMeetingRoomId(meetingRoomId=meetingRoom.getMeetingRoomId()).setHost(host = host).setStartTime(startTime=startTime).setEndTime(endTime=endTime).setDescription(description=description)
        
        for invitee in listOfUsers: 
            meeting.addInvitee(invitee)

        if not meetingRoom.addMeeting(meeting=meeting): 
            raise Exception("Meeting room not available for the input time period.")     
        self._sendEmailToUsers(users = listOfUsers, meeting=meeting)   
        
        return meeting
    
    def _sendEmailToUsers(self, users: list[User], meeting: Meeting) -> bool: 
        mail = self._getInviteMailFormat(meeting=meeting)
        for user in users: 
            self._mailService.sendEmailToUser(user = user, mail=mail)

    def addMeetingRoom(self, meetingRoom: MeetingRoom, user: User)->bool: 
        if user.isAdmin(): 
            if meetingRoom not in self._meetingRooms: 
                self._meetingRooms.append(meetingRoom)
                return True
            print("Meeting room already exists.")
        else:
            print("You do not have permission to add meeting rooms")
        return False
    
    def _getInviteMailFormat(self, meeting: Meeting) -> str:
        return f'''
                    Meeting Scheduled By Host: {meeting._host.getUserId()}
                    start time: {meeting.getStartTime()}
                    end time: {meeting.getEndTime()}
                    meeting room: {meeting.getMeetingRoomId()}
                    topic: {meeting.getDescription()}
            ''' 