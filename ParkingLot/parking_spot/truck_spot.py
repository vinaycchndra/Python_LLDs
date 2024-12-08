from parking_spot import ParkingSpot
from parking_spot_type import ParkingSpotType


class TruckSpot(ParkingSpot): 
    def __init__(self, parking_spot_id: str): 
        super().__init__(parking_spot_id = parking_spot_id, parking_spot_type = ParkingSpotType.LARGE)