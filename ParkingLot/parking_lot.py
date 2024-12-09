from parking_floor import ParkingFloor
from parking_spot.parking_spot import ParkingSpot
from entry_panel import EntryPanel
from exit_panel import ExitPanel

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
        self._listOfEntryPanels = []
        self._listOfExitPanels = [] 
    
    @classmethod
    def getInstance(cls): 
        return cls._instance
    
    def getListOfParkingFloor(self) -> list[ParkingFloor]: 
        return self._listOfParkingFloor
    
    def addParkingFloor(self, parking_floor: ParkingFloor)->None:
        self._listOfParkingFloor.append(parking_floor)
        return None
    
    def getParkingSpot(self, parking_spot_id : str) -> ParkingSpot:
        for parking_floor in self._listOfParkingFloor:
            parking_spot_map = parking_floor.getListOfParkingSpots()
            for parking_spots_key in parking_spot_map:
                for parking_spot in parking_spot_map.get(parking_spots_key):
                    if parking_spot.getParkingSpotId() == parking_spot_id:
                        return parking_spot
    
    def getListOfParkingFloors(self)->list[ParkingFloor]: 
        return self._listOfParkingFloor
    
    def getListOfEntryPanels(self)->list[EntryPanel]: 
        return self._listOfEntryPanels
    
    def getListOfExitPanels(self)->list[ExitPanel]: 
        return self._listOfExitPanels