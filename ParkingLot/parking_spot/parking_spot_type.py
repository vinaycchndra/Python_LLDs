from enum import Enum

# Enum for defining parking spot types.
class ParkingSpotType(Enum):
    COMPACT = "Compact"
    DISABLED = "Disabled"
    LARGE = "Large"
    MOTORCYCLE = "MotorCycle"
    ELECTRICCAR = "ElectricCar"