from .vehicle_type import VehicleType
from .vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self, registration_number: str):
        super().__init__(registration_number=registration_number, vehicle_type=VehicleType.TRUCK)
        

