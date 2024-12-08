from parking_spot.parking_spot_type import ParkingSpotType
from display_board import DisplayBoard
from vehicle.vehicle import Vehicle
from vehicle.vehicle_type import VehicleType

class ParkingFloor:
    def __init__(self, parking_floor_id: str, ):
        self._parkingFloorId = parking_floor_id
        self._displayBoard  = DisplayBoard()
        self._parkingSpotMap = {parking_spot : [] for parking_spot in ParkingSpotType}

    def getParkingFloorId(self) -> str:
        return self._parkingFloorId 
    
    def getListOfParkingSpots(self) -> dict[list[str]]: 
        return self._parkingSpotMap
    
    def showDisplayBoard(self):
        display_message = ["Available Spot Counts: "]
        
        for key in self._parkingSpotMap: 
            count = 0
            for  spot in self._parkingSpotMap.get(key):
                if spot.isSpotFree(): 
                    count += 1
            display_message.append("%s :: %d" % (key, count))
        
        self._displayBoard("\n".join(display_message))

    def _getSpotTypeForVehicle(self, vehicle_type: VehicleType):
        if vehicle_type == VehicleType.CAR:
            return ParkingSpotType.COMPACT
        elif vehicle_type == VehicleType.MOTORCYCLE:
            return ParkingSpotType.MOTORCYCLE
        elif vehicle_type == VehicleType.TRUCK:
            return ParkingSpotType.LARGE
        elif vehicle_type == VehicleType.ELECTRICCAR:
            return ParkingSpotType.ELECTRICCAR
        elif vehicle_type == VehicleType.VAN:
            return ParkingSpotType.COMPACT
        return ParkingSpotType.LARGE

    def getAvailableSpot(self, vehicle: Vehicle):
        for spot in self._parkingSpotMap.get(self._getSpotTypeForVehicle(vehicle.getVehicleType())): 
            if spot.isSpotFree():
                return spot
        return None
    
    def getInUseSpotsForVehicleType(self, vehicle_type: VehicleType):
        in_use_parking_spots = []
        for spot in self._parkingSpotMap.get(self._getSpotTypeForVehicle(vehicle_type)):
            if not spot.isSpotFree():
                in_use_parking_spots.append(spot)
        return in_use_parking_spots