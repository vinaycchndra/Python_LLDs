from parking_spot.parking_spot_type import ParkingSpotType

class HourlyCost:
    def __init__(self):
        self._hourlyCosts = dict()

        self._hourlyCosts[ParkingSpotType.COMPACT] = 30
        self._hourlyCosts[ParkingSpotType.DISABLED] = 10
        self._hourlyCosts[ParkingSpotType.LARGE] = 50
        self._hourlyCosts[ParkingSpotType.MOTORCYCLE] = 15
        self._hourlyCosts[ParkingSpotType.ELECTRICCAR] = 40

    def getHourlyCost(self, parking_spot_type: ParkingSpotType) -> float: 
        if parking_spot_type in self._hourlyCosts: 
            return self._hourlyCosts.get(parking_spot_type)
        raise Exception(f"There is no cost associated with the {parking_spot_type} type.")
    