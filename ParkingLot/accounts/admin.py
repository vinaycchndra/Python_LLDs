from parking_floor import ParkingFloor
from parking_lot import ParkingLot
from accounts import Account
from parking_spot.parking_spot import ParkingSpot
from entry_panel import EntryPanel
from exit_panel import ExitPanel

class Admin(Account): 
    def __init__(self, username: str, password: str):
        super().__init__(username=username, password=password)

    def addParkingFloor(self, parking_floor: ParkingFloor) -> bool:
        parkin_lot = ParkingLot.getInstance()
        for parking_floor_ in parkin_lot.getListOfParkingFloors():
            if parking_floor_.getParkingFloorId() == parking_floor.getParkingFloorId(): 
                return False
        parkin_lot._listOfParkingFloor.append(parking_floor)
        return True
        
    def addParkingSpot(self, parking_floor_id: str, parking_spot: ParkingSpot) -> None: 
        parkin_lot = ParkingLot.getInstance()
        parking_floor = None
        for parking_floor_ in parkin_lot.getListOfParkingFloors():
            if parking_floor_.getParkingFloorId() == parking_floor_id: 
                parking_floor = parking_floor_
                break

        if parking_floor is None: 
            raise Exception(f"No such parking floor with parking floor id: {parking_floor_id}")
        
        parking_spot_type = parking_spot.getParkingSpotType()
        parking_spot_arr = parking_floor.getListOfParkingSpots().get(parking_spot_type)
        
        if parking_spot_arr is None: 
            raise Exception("Not a valid parking spot type")

        for parking_spot_ in parking_spot_arr: 
            if parking_spot_.getParkingSpotId() == parking_spot.getParkingSpotId():
                    raise Exception(f"Parking spot already exists with parking spot id : {parking_spot.getParkingSpotId()}") 
        
        parking_spot_arr.append(parking_spot)
        
    def addEntryPanel(self, entry_panel: EntryPanel) -> None: 
        parkin_lot = ParkingLot.getInstance()

        entry_panels = parkin_lot.getListOfEntryPanels()

        for entry_panel_ in entry_panels: 
            if entry_panel_.getEntryPanelId() == entry_panel.getEntryPanelId():
                raise Exception("Entry panel already exists.")
        entry_panels.append(entry_panel)

    def addExitPanel(self, exit_panel: ExitPanel) -> None: 
        parkin_lot = ParkingLot.getInstance()

        exit_panels = parkin_lot.getListOfExitPanels()

        for exit_panel_ in exit_panels: 
            if exit_panel_.getExitPanelId() == exit_panel.getExitPanelId():
                raise Exception("Exit panel already exists.")
        exit_panels.append(exit_panel)