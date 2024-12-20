import unittest
from meeting import Meeting
from basic_calendar import Calendar
from account.user import User
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
            
if __name__ == "__main__": 
    unittest.main()