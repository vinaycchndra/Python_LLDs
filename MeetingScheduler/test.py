import unittest
from meeting import Meeting
from basic_calendar import Calendar
from account.user import User
from account.admin import Admin
from meeting_room import MeetingRoom
from email_service import EmailService
from meeting_scheduler import MeetingScheduler
from datetime import datetime, timedelta

class TestMeetingScheduler(unittest.TestCase): 
    def test_meeting(self): 
        meeting_id = "meeting_1"
        meeting_room_id = "meeting_room_1"
        host = User(password="user@123", userId = "user")
        invitee_1 = User(password="user1@123", userId = "user1")
        invitee_2 = User(password="user2@123", userId = "user2")
        invitee_3 = User(password="user3@123", userId = "user3")
        invitee_4 = User(password="user4@123", userId = "user4")
        invitee_5 = User(password="user5@123", userId = "user5")
        description = "Discussion on architecture design of the product."
        start_time = datetime.now()
        end_time = start_time+timedelta(hours=1)
        meeting = Meeting(meetingId=meeting_id)
        meeting.setStartTime(startTime=start_time).setEndTime(endTime=end_time).\
        setDescription(description=description).setMeetingRoomId(meetingRoomId=meeting_room_id).\
        setHost(host=host).addInvitee(user=invitee_1).addInvitee(user=invitee_2).addInvitee(user=invitee_3)\
        .addInvitee(user=invitee_4).addInvitee(user=invitee_5)

        self.assertEqual(start_time, meeting.getStartTime())
        self.assertEqual(end_time, meeting.getEndTime())
        self.assertEqual(host, meeting.getHost())
        self.assertEqual(description, meeting.getDescription())
        self.assertEqual(set([invitee_1, invitee_2, invitee_3, invitee_4, invitee_4, invitee_5]), set(meeting.getListOfInvitees()))    

    def test_calendar(self): 
        calendar = Calendar(calendarId="calendar_1", meetingRoomId="meeting_room_1")
        
        # meeting 1
        meeting_1 = Meeting(meetingId="meeting_1")
        start_time_1 = datetime.now()
        end_time_1= start_time_1+timedelta(hours=1, minutes=30)
        meeting_1.setStartTime(startTime=start_time_1).setEndTime(endTime=end_time_1)
        calendar.addMeetingToCalendar(meeting=meeting_1)

        # meeting 2
        meeting_2 = Meeting(meetingId="meeting_2")
        start_time_2 = end_time_1+timedelta(minutes=40)
        end_time_2= start_time_2+timedelta(hours=1)
        meeting_2.setStartTime(startTime=start_time_2).setEndTime(endTime=end_time_2)
        calendar.addMeetingToCalendar(meeting=meeting_2)
        
        # new meeting timing which actually overlaps with the first meeting should return not available 
        start_time_3 = start_time_1+timedelta(minutes = 5)
        end_time_3   = end_time_1-timedelta(minutes=5)
        self.assertEqual(calendar.checkAvailability(startTime=start_time_3, endTime=end_time_3), False)
        
        # new timing which is between the meeting 1 and meeting 2 should be available to shedule the meeting.
        start_time_4 = end_time_1+timedelta(minutes = 5)
        end_time_4   = start_time_4+timedelta(minutes=30)
        meeting_4 = Meeting(meetingId="meeting_4")
        self.assertEqual(calendar.checkAvailability(startTime=start_time_4, endTime=end_time_4), True)
        
        meeting_4.setStartTime(startTime=start_time_4).setEndTime(endTime=end_time_4)
        calendar.addMeetingToCalendar(meeting=meeting_4)
        
        # new meeting time after meeting 2 should be available
        start_time_5 = end_time_2
        end_time_5   = start_time_5+timedelta(minutes=40)
        self.assertEqual(calendar.checkAvailability(startTime=start_time_5, endTime=end_time_5), True)
    
    def test_meetingRoom(self):
        meeting_room_id = "meeting_room_1"
        meeting_room_capacity = 10
        calendar = Calendar(calendarId="calendar_1", meetingRoomId=meeting_room_id) 
        meeting_room_1 = MeetingRoom(meetingRoomId=meeting_room_id, calendar=calendar, capacity=meeting_room_capacity)
        
        meeting = Meeting(meetingId="meeting")
        start_time = datetime.now()
        end_time= start_time+timedelta(hours=1, minutes=30)
        meeting.setStartTime(startTime=start_time).setEndTime(endTime=end_time)
        
        self.assertEqual(meeting_room_id, meeting_room_1.getMeetingRoomId())
        self.assertEqual(meeting_room_capacity, meeting_room_1.getMeetingRoomCapacity())
        self.assertEqual(True, meeting_room_1.isAvailable(startTime=start_time, endTime=end_time))    
        
        meeting_room_1.addMeeting(meeting=meeting)
        self.assertFalse(meeting_room_1.isAvailable(startTime=start_time, endTime=end_time))

    def test_EmailService(self): 
        email_service = EmailService()
        
        user1 = User(password="user1@123", userId = "user1")
        user2 = User(password="user2@123", userId = "user2")
        user3 = User(password="user3@123", userId = "user3")
        description = "Discussion on architecture design of the product."
        email_service.sendEmailToUser(user1, mail=description)
        email_service.sendEmailToUser(user2, mail=description)
        email_service.sendEmailToUser(user3, mail=description)
        
        self.assertEqual(user1.getMyMails(), [description])
        self.assertEqual(user2.getMyMails(), [description])
        self.assertEqual(user3.getMyMails(), [description])

    def test_MeetingScheduler(self): 

        user1 = User(password="user1@123", userId = "user1")
        user2 = User(password="user2@123", userId = "user2")
        user3 = User(password="user3@123", userId = "user3")
        user4 = User(password="user4@123", userId = "user4")
        user5 = User(password="user5@123", userId = "user5")
        user6 = User(password="user6@123", userId = "user6")
        user7 = User(password="user7@123", userId = "user7")
        user8 = User(password="user8@123", userId = "user8")
        user9 = User(password="user9@123", userId = "user9")
        user10 = User(password="user10@123", userId = "user10")
        user_list = [user1, user2, user3, user4, user5, user6, user7, user8, user9, user10]

        calendar_1 = Calendar(calendarId="calendar_1", meetingRoomId="meeting_room_1") 
        meeting_room_1 = MeetingRoom(meetingRoomId="meeting_room_1", calendar=calendar_1, capacity=4)
        
        calendar_2 = Calendar(calendarId="calendar_2", meetingRoomId="meeting_room_2") 
        meeting_room_2 = MeetingRoom(meetingRoomId="meeting_room_2", calendar=calendar_2, capacity=5)
        
        calendar_3 = Calendar(calendarId="calendar_3", meetingRoomId="meeting_room_3") 
        meeting_room_3 = MeetingRoom(meetingRoomId="meeting_room_3", calendar=calendar_3, capacity=5)

        calendar_4 = Calendar(calendarId="calendar_4", meetingRoomId="meeting_room_4") 
        meeting_room_4 = MeetingRoom(meetingRoomId="meeting_room_4", calendar=calendar_4, capacity=6)

        calendar_5 = Calendar(calendarId="calendar_5", meetingRoomId="meeting_room_5") 
        meeting_room_5 = MeetingRoom(meetingRoomId="meeting_room_5", calendar=calendar_5, capacity=8)

        calendar_6 = Calendar(calendarId="calendar_6", meetingRoomId="meeting_room_6") 
        meeting_room_6 = MeetingRoom(meetingRoomId="meeting_room_6", calendar=calendar_6, capacity=10)        
        
        
        meeting_scheduler =  MeetingScheduler()
        # Testing singleton method use.
        self.assertEqual(meeting_scheduler.getInstance(), MeetingScheduler())
        
        admin = Admin(userId="admin", password="admin@123")
        self.assertTrue(admin.addNewMeetingRoomToScheduler(meetingRoom = meeting_room_1))
        self.assertTrue(admin.addNewMeetingRoomToScheduler(meetingRoom = meeting_room_2))
        self.assertTrue(admin.addNewMeetingRoomToScheduler(meetingRoom = meeting_room_3))
        self.assertTrue(admin.addNewMeetingRoomToScheduler(meetingRoom = meeting_room_4))
        self.assertTrue(admin.addNewMeetingRoomToScheduler(meetingRoom = meeting_room_5))
        self.assertTrue(admin.addNewMeetingRoomToScheduler(meetingRoom = meeting_room_6))

        # Only 5 meeting rooms should be available out of 6 for 5 people meeting
        self.assertEqual(5, meeting_scheduler.getAvailableMeetingRooms(startTime=datetime.now(), endTime=datetime.now()+timedelta(hours=1), capacity=5).__len__())
        self.assertEqual(6, meeting_scheduler.getAvailableMeetingRooms(startTime=datetime.now(), endTime=datetime.now()+timedelta(hours=1), capacity=4).__len__())
        self.assertEqual(2, meeting_scheduler.getAvailableMeetingRooms(startTime=datetime.now(), endTime=datetime.now()+timedelta(hours=1), capacity=8).__len__())

        # meeting 1 
        start_time = datetime.now()
        end_time = start_time+timedelta(hours=1)

        meeting_1_scheduled = meeting_scheduler.bookMeeting(host = user1, meetingRoom=meeting_room_6, startTime=start_time, endTime=end_time, description="client meeting", listOfUsers=user_list)
        self.assertEqual(meeting_1_scheduled.getListOfInvitees(), user_list)
        self.assertEqual(meeting_1_scheduled.getHost(), user1)
        self.assertRaises(Exception, meeting_scheduler.bookMeeting, user1, meeting_room_6, start_time, end_time, "client meeting", user_list)
        self.assertEqual(5, meeting_scheduler.getAvailableMeetingRooms(startTime=start_time, endTime=end_time, capacity=4).__len__())
        
if __name__ == "__main__": 
    unittest.main()