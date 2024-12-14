from vehicle.vehicle import Vehicle
from parking_ticket import ParkingTicket
from datetime import datetime
import uuid
from parking_lot import ParkingLot
from parking_floor import ParkingFloor
from parking_spot.parking_spot import ParkingSpot

class EntryPanel:
    def __init__(self, entry_panel_id: str):
        self._entryPanelId = entry_panel_id

    def getEntryPanelId(self):
        return self._entryPanelId
    
    def getParkingTicket(self, vehicle: Vehicle) -> ParkingTicket:
        parking_lot = ParkingLot.getInstance()
        parking_floors = parking_lot.getListOfParkingFloor()

        parking_spot_for_vehicle = None
        parking_floor_for_vehicle = None

        for parking_floor in parking_floors: 
            parking_spot_for_vehicle =  parking_floor.getAvailableSpot(vehicle)
            if parking_spot_for_vehicle is not None:
                parking_floor_for_vehicle = parking_floor
                break
        
        # if no parking spot is available can not generate a ticket
        if parking_spot_for_vehicle is None:
            print("No parking space available.")
            return None
        
        parking_spot_for_vehicle.assignVehicleToSpot(vehicle)
        return self._genetateParkingTicket(vehicle=vehicle, floor_id=parking_floor_for_vehicle.getParkingFloorId(), spot_id=parking_spot_for_vehicle.getParkingSpotId())

    def _genetateParkingTicket(self, vehicle: Vehicle, floor_id : str, spot_id : str) -> ParkingTicket: 
        parking_ticket = ParkingTicket(
                                    parking_ticket_id = uuid.uuid4(),
                                    vehicle_registration_id = vehicle.getRegistrationNumber(), 
                                    parking_floor_id = floor_id, 
                                    parking_spot_id=spot_id, 
                                    vehicle_type = vehicle.getVehicleType()
                                )
        
        return parking_ticket.setStartTime(start_time = datetime.now())

        
    
