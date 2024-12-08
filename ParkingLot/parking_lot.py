from parking_floor import ParkingFloor

class ParkingLot:
    _instance = None
    # Singleton class using New method this allocates the memory and after this the init method is 
    # called for the object's attribute initialisation.

    def __new__(cls, *args, **kwargs):
        if cls._instance is None: 
            cls._instance = super().__new__(cls, *args, **kwargs) 
        return cls._instance
    
    def __init__(self): 
        self._listOfParkingFloor = [] 
    
    @classmethod
    def getInstance(cls): 
        return cls._instance
    
    def getListOfParkingFloor(self) -> list[ParkingFloor]: 
        return self._listOfParkingFloor
    
    def addParkingFloor(self, parking_floor: ParkingFloor)->None:
        self._listOfParkingFloor.append(parking_floor)
        return None