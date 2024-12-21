from vehicle.vehicle import Vehicle
from .parking_spot_type import ParkingSpotType

class ParkingSpot: 
    def __init__(self, parking_spot_id: str, parking_spot_type: ParkingSpotType):
        self._parkingSpotId = parking_spot_id
        self._isSpotAvailable = True
        self._parkingSpotType = parking_spot_type
        self._vehicle = None
        
    def getParkingSpotId(self) ->  str:
        return self._parkingSpotId
    
    def getParkingSpotType(self) -> ParkingSpotType:
        return self._parkingSpotType
     
    def isSpotFree(self) -> bool:
        return self._isSpotAvailable
    
    def getVehicleDetails(self) -> Vehicle:
        return self._vehicle
    
    def assignVehicleToSpot(self, vehicle: Vehicle) -> bool:
        if self._vehicle is None:
            self._vehicle = vehicle
            self._isSpotAvailable = False
            return True
        return False

    def vacateVehicleFromSpot(self) -> bool:
        self._vehicle = None
        self._isSpotAvailable = True
        return True
         

