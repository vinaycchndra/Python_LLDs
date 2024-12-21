from user import User
from meeting_room import MeetingRoom
from meeting_scheduler import MeetingScheduler

class Admin(User): 
    def __init__(self, userId: str, password: str): 
        super().__init__(self, userId = userId, password=password)
        self._admin = True

    def addNewMeetingRoomToScheduler(meetingRoom: MeetingRoom) -> bool: 
        try: 
            return MeetingScheduler.getInstance().addMeetingRoom(meetingRoom)
        except Exception as e: 
            print(e)
        return False