import unittest
from uuid import uuid4
from parking_spot.parking_spot_type import ParkingSpotType
from parking_spot.parking_spot import ParkingSpot
from vehicle.car import Car
from vehicle.vehicle_type import VehicleType

class TestParkingLotsEntities(unittest.TestCase): 
    def test_parking_spot(self): 
        parking_spot = ParkingSpot(uuid4(), ParkingSpotType.COMPACT)
        car = Car(uuid4())

        self.assertEqual(parking_spot.isSpotFree(), True)
        self.assertEqual(parking_spot.getVehicleDetails(), None)
        # Assigning vehicle to spot
        parking_spot.assignVehicleToSpot(vehicle=car)
        
        self.assertEqual(parking_spot.isSpotFree(), False)
        self.assertEqual(parking_spot.getVehicleDetails(), car)

        # vacating vehicle from the spot 
        parking_spot.assignVehicleToSpot(vehicle=car)
        parking_spot.vacateVehicleFromSpot()
        self.assertEqual(parking_spot.isSpotFree(), True)
        
if __name__ == "__main__": 
    unittest.main()