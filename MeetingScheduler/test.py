import unittest
from meeting import Meeting
from basic_calendar import Calendar
from datetime import datetime, timedelta

class TestMeetingScheduler(unittest.TestCase): 
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