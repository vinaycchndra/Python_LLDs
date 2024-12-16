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
            Queries the available room for the follwing parameters - (start_time, end_time,  capacity) - which should show the list of the available rooms with input slots.  Once the meeting rooms are available we can choose from the room of our own choice and book the calendar of that meeting room for that time slot. Once the meeting room is booked it should send the meeting notification to all the users for the meeting. We should be able to update the meetings with the invitees and timing of the meeting and room also.
    </p>
    <p align="center">
        <img src="/docs/activity_diagram.png" alt="Activity Diagram">
            <br />
        Activity diagram for Meeting Scheduler
    </p>



    