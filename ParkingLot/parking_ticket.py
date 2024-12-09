from vehicle.vehicle_type import VehicleType
from datetime import datetime
class ParkingTicket: 
    def __init__(self, 
                parking_ticket_id: str, 
                vehicle_registration_id: str, 
                parking_floor_id: str,
                parking_spot_id: str, 
                vehicle_type: VehicleType): 
        self._parkingTicketId = parking_ticket_id
        self._vehicleRegistrationId = vehicle_registration_id
        self._parkingFloorId = parking_floor_id 
        self._parkingSpotId = parking_spot_id
        self._vehicleType = vehicle_type
        self._startTime = None
        self._endTime = None
        self._amount = 0
    
    def getParkingTicketId(self) -> str:
        return self._parkingTicketId 
    
    def getVehicleRegistrationNumber(self) -> str: 
        return self._vehicleRegistrationId
    
    def getParkingSpotId(self) -> str: 
        return self._parkingSpotId
    
    def getParkingFloorId(self) -> str:
        return self._parkingFloorId

    def getVehicleType(self) -> VehicleType:
        return self._vehicleType
      
    def setStartTime(self, start_time: datetime)->None:
        self._startTime = start_time
        return self

    def setEndTime(self, end_time: datetime)->None:
        self._endTime = end_time
        return self
    
    def getStartTime(self) -> datetime: 
        return self._startTime
    
    def getEndTime(self) -> datetime: 
        return self._endTime
    
    def getAmount(self) -> float:
        pass

    def setAmount(self, amount: float)-> None:
        self._amount = amount
    
