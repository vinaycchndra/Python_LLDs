from .vehicle_type import VehicleType

class Vehicle: 
    def __init__(self, registration_number: str, vehicle_type: VehicleType):
        self._registrationNumber = registration_number
        self._vehicle_type = vehicle_type

    def getRegistrationNumber(self):
        return self._registrationNumber
    
    def getVehicleType(self):
        return self._vehicle_type