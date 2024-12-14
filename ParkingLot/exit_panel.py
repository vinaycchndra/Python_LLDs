from parking_ticket import ParkingTicket
from hourly_cost import HourlyCost
from datetime import datetime
from parking_lot import ParkingLot
from parking_spot.parking_spot import ParkingSpotType

class ExitPanel:
    def __init__(self, exit_panel_id: str):
        self._exitPanelId = exit_panel_id

    def getExitPanelId(self) -> str:
        return self._exitPanelId
    
    def checkOut(self, parking_ticket: ParkingTicket): 
        parking_lot = ParkingLot.getInstance()
        parking_spot = parking_lot.getParkingSpot(parking_ticket.getParkingSpotId())
        parking_spot.vacateVehicleFromSpot()
        parking_ticket.setAmount(self._calculateAmount(parking_spot_type = parking_spot.getParkingSpotType(),duration = self._calculateHours(parking_ticket)))

    def _calculateHours(self, parking_ticket: ParkingTicket) -> float:
        parking_ticket = parking_ticket.setEndTime(datetime.now())
        total_time = parking_ticket.getEndTime() - parking_ticket.getStartTime()
        total_hours = total_time.total_seconds()/3600
        return total_hours

    def _calculateAmount(self, parking_spot_type: ParkingSpotType, duration: float) -> float: 
        if duration < 1: 
            duration = 1
        cost_config = HourlyCost()
        return duration * cost_config.getHourlyCost(parking_spot_type)
