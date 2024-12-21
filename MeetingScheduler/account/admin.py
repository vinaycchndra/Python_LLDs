from account.user import User
from meeting_room import MeetingRoom
from meeting_scheduler import MeetingScheduler

class Admin(User): 
    def __init__(self, userId: str, password: str): 
        super().__init__(userId = userId, password=password)
        super()._setUserAsAdmin()

    def addNewMeetingRoomToScheduler(self, meetingRoom: MeetingRoom) -> bool: 
        try: 
            return MeetingScheduler.getInstance().addMeetingRoom(meetingRoom = meetingRoom, user = self)
        except Exception as e: 
            print(e)
        return False