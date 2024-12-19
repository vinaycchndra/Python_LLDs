<h3> Problem Statement </h3>
    <p>
        <ul>
            <li>
                Given n meeting rooms. User should be able to book any meeting room with the capacity and availability of the room  based upon the start time and end time of the meeting with notification being sent to the invitees of the meeting.
            </li>
            <li>
                You should use calender for tracking date and time and every meeting room should have its own calendar.
            </li>
            <li> 
                And also history of all the meetings which are booked and asscociated meeting rooms. 
            </li>
        </ul>
    </p>

<h3> Activity Diagram </h3>
    <p> User interacts and calls to the meeting scheduler: 
            <ul>
                <li>
                 Queries the available room for the follwing parameters - (start_time, end_time,  capacity) - which should show the list of the available rooms with input slots. 
                </li>
                <li>             
                    Once the meeting rooms are available we can choose from the room of our own choice and book the calendar of that meeting room for that time slot. 
                </li>
                <li>
                    Once the meeting room is booked it should send the meeting notification to all the users for the meeting. We should be able to update the meetings with the invitees and timing of the meeting and room also.
                </li>
            </ul>
    </p>
    <p align="center">
        <img src="/MeetingScheduler/docs/activity_diagram.png" alt="Activity Diagram">
            <br />
        Activity diagram for Meeting Scheduler
    </p>

<h3> Class Diagram </h3>

```mermaid
classDiagram
    class MeetingScheduler{
    - meetingRooms: Array~MeetingRooms~
    + getInstance(): self
    + getAvailableMeetingRooms(startTime: DateTime, endTime: DateTime, capacity: int): MeetingRoom[]
    + bookMeeting(startTime: DateTime, endTime: DateTime, listOfUsers: User[]): Meeting
    - sendEmailToUsers(users: User[], meeting: Meeting): boolean
    - getInviteMailFormat(meeting: Meeting): str
    + addMeetingRoom(meetingRoom: MeetingRoom, user: User): boolean
    }

    MeetingScheduler --> MeetingRoom: Association 
    MeetingScheduler --> EmailService: Association

    class EmailService{
        + sendEmailToUser(user: User, mail: str): null
    }

    class MeetingRoom{
        - meetingRoomId: string
        - calendar: Calendar
        - capacity: integer
        + getMeetingRoomCapacity(): integer
        + getMeetingRoomId(): string
        + addMeeting(meeting: Meeting): boolean
        + isAvailable(startTime: DateTime, endTime: DateTime): boolean
    }

    class Calendar{
        - calendarId: string
        - meetingRoomId: string
        - scheduledMeetings: Array~Meeting~
        + addMeetingToCalendar(meeting: Meeting): null
        + checkAvailability(startTime: DateTime, endTime: DateTime): boolean
    }
    
    MeetingRoom --> Calendar: Association
    Calendar *-- Meeting: Composition
    
    class User{
        - userId: string
        - password: string
        - isAdmin: bool = False
        + isAdmin(): boolean
        + getMail(message: string): null 
        + getUserId(): string
    }

    User <|-- Admin: Extends
    
    class Admin{
        - isAdmin: bool = True
        + addNewMeetingRoomToScheduler(meetingRoom: MeetingRoom): boolean
    }

    class Meeting{
        - meetingId: string
        - meetingRoomId: string
        - host: User
        - invitees: Array~Users~
        - description: string
        - startTime: DateTime
        - endTime: DateTime
        + getMeetingId(): string
        + getMeetingRoomId(): string
        + getHost(): User
        + getListOfInvitees(): User[]
        + getDescription(): string
        + setDescription(): self
        + setMeetingRoomId(meetingRoomId: string): self
        + setHost(host: User): self
        + addInvitee(user: User): self
        + setStartTime(startTime: DateTime): self
        + setEndTime(endTime: DateTime): self
        + getStartTime(): datetime
        + getEndTime(): datetime
    }

    Meeting o-- User: Aggregation
```


    