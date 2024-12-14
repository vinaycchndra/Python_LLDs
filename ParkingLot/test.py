import unittest
import time
from uuid import uuid4
from parking_spot.parking_spot_type import ParkingSpotType
from parking_spot.parking_spot import ParkingSpot
from vehicle import car, truck, motorcycle, electriccar
from accounts.admin import Admin
from parking_floor import ParkingFloor
from parking_lot import ParkingLot
from vehicle.vehicle_type import VehicleType
from entry_panel import EntryPanel
from exit_panel import ExitPanel
from hourly_cost import HourlyCost

class TestParkingLotsEntities(unittest.TestCase): 
    def test_parking_spot(self): 
        parking_spot = ParkingSpot(uuid4(), ParkingSpotType.COMPACT)
        car_ = car.Car(uuid4())

        self.assertEqual(parking_spot.isSpotFree(), True)
        self.assertEqual(parking_spot.getVehicleDetails(), None)
        # Assigning vehicle to spot
        parking_spot.assignVehicleToSpot(vehicle=car_)
        
        self.assertEqual(parking_spot.isSpotFree(), False)
        self.assertEqual(parking_spot.getVehicleDetails(), car_)

        # vacating vehicle from the spot 
        parking_spot.assignVehicleToSpot(vehicle=car_)
        parking_spot.vacateVehicleFromSpot()
        self.assertEqual(parking_spot.isSpotFree(), True)

    def test_parking_floor(self): 
        ParkingLot() 
        parking_lot = ParkingLot.getInstance()
        # Adding parking floors by the admin user
        admin = Admin(username='user', password='user@123')        
        added_parking_floors = []
        
        for i in range(1,5):
            parking_floor_ = ParkingFloor(parking_floor_id='parking_floor_%s'%i)
            added_parking_floors.append(parking_floor_)
            admin.addParkingFloor(parking_floor=parking_floor_)
        
        # adding two parking spots of single parking_spot_type in every parking floor 
        for parking_spot_type in ParkingSpotType:
            if parking_spot_type == ParkingSpotType.DISABLED:
                continue
            admin.addParkingSpot('parking_floor_1', ParkingSpot(parking_spot_id=f'{parking_spot_type.name}_a_parking_floor_1', parking_spot_type = parking_spot_type))    
            admin.addParkingSpot('parking_floor_1',ParkingSpot(parking_spot_id=f'{parking_spot_type.name}_b_parking_floor_1', parking_spot_type = parking_spot_type))    
            admin.addParkingSpot('parking_floor_2',ParkingSpot(parking_spot_id=f'{parking_spot_type.name}_a_parking_floor_2', parking_spot_type = parking_spot_type))    
            admin.addParkingSpot('parking_floor_2',ParkingSpot(parking_spot_id=f'{parking_spot_type.name}_b_parking_floor_2', parking_spot_type = parking_spot_type))    
            admin.addParkingSpot('parking_floor_3',ParkingSpot(parking_spot_id=f'{parking_spot_type.name}_a_parking_floor_3', parking_spot_type = parking_spot_type))    
            admin.addParkingSpot('parking_floor_3',ParkingSpot(parking_spot_id=f'{parking_spot_type.name}_b_parking_floor_3', parking_spot_type = parking_spot_type))    
            admin.addParkingSpot('parking_floor_4',ParkingSpot(parking_spot_id=f'{parking_spot_type.name}_a_parking_floor_4', parking_spot_type = parking_spot_type))    
            admin.addParkingSpot('parking_floor_4',ParkingSpot(parking_spot_id=f'{parking_spot_type.name}_b_parking_floor_4', parking_spot_type = parking_spot_type))    
        
        for parking_floor_ in parking_lot.getListOfParkingFloor():
            for vehicle_type_ in VehicleType:
                # checking if the available parking spots are in sync with what spots are added.
                self.assertEqual(0, len(parking_floor_.getInUseSpotsForVehicleType(vehicle_type_)))
                
        for parking_floor_ in parking_lot.getListOfParkingFloor():
            car_vehicle = car.Car(registration_number='car_1_%s'%parking_floor_.getParkingFloorId())
            car_spot = parking_floor_.getAvailableSpot(car_vehicle)
            car_spot.assignVehicleToSpot(car_vehicle)

            truck_vehicle = truck.Truck(registration_number='truck_1_%s'%parking_floor_.getParkingFloorId())
            truck_spot = parking_floor_.getAvailableSpot(truck_vehicle)
            truck_spot.assignVehicleToSpot(truck_vehicle)
            
            electriccar_vehicle = electriccar.ElectricCar(registration_number='electriccar_1_%s'%parking_floor_.getParkingFloorId())
            electriccar_spot = parking_floor_.getAvailableSpot(electriccar_vehicle)
            electriccar_spot.assignVehicleToSpot(electriccar_vehicle)
            
            motorcycle_vehicle = motorcycle.MotorCycle(registration_number='motorcycle_1_%s'%parking_floor_.getParkingFloorId())
            motorcycle_spot = parking_floor_.getAvailableSpot(motorcycle_vehicle)
            motorcycle_spot.assignVehicleToSpot(motorcycle_vehicle)
            
        for parking_floor_ in parking_lot.getListOfParkingFloor():
            for vehicle_type_ in VehicleType:
                # checking if the available parking spots are in sync after one spot of every type is occupied by the vehicle.
                if vehicle_type_ == VehicleType.VAN:
                    continue
                self.assertEqual(1, len(parking_floor_.getInUseSpotsForVehicleType(vehicle_type_)))
        
        # Available spots for the parking spots by display board test.
        output_message_list = ["Available Spot Counts: "]
        for parking_spot_type in ParkingSpotType:
            if parking_spot_type != ParkingSpotType.DISABLED:
                output_message_list.append("%s :: %d" % (parking_spot_type, 1))
            else:
                output_message_list.append("%s :: %d" % (parking_spot_type, 0))

        # Display board messages testing.
        output_message = "\n".join(output_message_list)
        for parking_floor_ in added_parking_floors: 
            self.assertEqual(output_message, parking_floor_.showDisplayBoard())

    def test_entry_and_exit_panel(self):
        ParkingLot() 
        entry_panel = EntryPanel(entry_panel_id="entry_panel_1")
        exit_panel = ExitPanel(exit_panel_id="exit_panel_1")
        hourly_cost = HourlyCost()
        # Adding parking floors by the admin user
        admin = Admin(username='user', password='user@123')        
        parking_floor_1 =  ParkingFloor(parking_floor_id='parking_floor_1')
        parking_floor_2 =  ParkingFloor(parking_floor_id='parking_floor_2')
        admin.addParkingFloor(parking_floor_1)
        admin.addParkingFloor(parking_floor_2)
        
        # adding parking spots 
        admin.addParkingSpot('parking_floor_1', ParkingSpot(parking_spot_id=f'{ParkingSpotType.COMPACT.name}_a_parking_floor_1', parking_spot_type = ParkingSpotType.COMPACT))    
        admin.addParkingSpot('parking_floor_1',ParkingSpot(parking_spot_id=f'{ParkingSpotType.LARGE.name}_b_parking_floor_1', parking_spot_type = ParkingSpotType.LARGE))    
        admin.addParkingSpot('parking_floor_2',ParkingSpot(parking_spot_id=f'{ParkingSpotType.COMPACT.name}_a_parking_floor_2', parking_spot_type = ParkingSpotType.COMPACT))    
        admin.addParkingSpot('parking_floor_2',ParkingSpot(parking_spot_id=f'{ParkingSpotType.LARGE.name}_b_parking_floor_2', parking_spot_type = ParkingSpotType.LARGE))    
        
        # Creating Vehicles for parking spots 
        vehicle_1 = car.Car(registration_number=uuid4())
        vehicle_2 = truck.Truck(registration_number=uuid4())
        vehicle_3 = car.Car(registration_number=uuid4())
        vehicle_4 = truck.Truck(registration_number=uuid4())
        vehicle_5 = car.Car(registration_number=uuid4())
        vehicle_6 = truck.Truck(registration_number=uuid4())
        
        # getting parking tickets
        parking_ticket_vehicle_1 = entry_panel.getParkingTicket(vehicle_1)
        parking_ticket_vehicle_2 = entry_panel.getParkingTicket(vehicle_2)
        parking_ticket_vehicle_3 = entry_panel.getParkingTicket(vehicle_3)
        parking_ticket_vehicle_4 = entry_panel.getParkingTicket(vehicle_4)
        
        self.assertEqual(parking_ticket_vehicle_1.getParkingFloorId() in ("parking_floor_1", "parking_floor_2"), True)
        self.assertEqual(parking_ticket_vehicle_2.getParkingFloorId() in ("parking_floor_1", "parking_floor_2"), True)
        self.assertEqual(parking_ticket_vehicle_3.getParkingFloorId() in ("parking_floor_1", "parking_floor_2"), True)
        self.assertEqual(parking_ticket_vehicle_4.getParkingFloorId() in ("parking_floor_1", "parking_floor_2"), True)
        
        # Should not get the ticket now as no parking spots are available.
        self.assertEqual(entry_panel.getParkingTicket(vehicle_5), None)
        self.assertEqual(entry_panel.getParkingTicket(vehicle_6), None)

        print("Will sleep for 10 seconds to get some time for the vehicle to occupy spots for atleast 10 seconds.")
        time.sleep(5)

        # Making spots available for the the vehicle 5 and 6 by checking out vehicle_3 and vehicle_4
        self.assertEqual(parking_ticket_vehicle_3.getAmount(), 0)
        self.assertEqual(parking_ticket_vehicle_4.getAmount(), 0)
        exit_panel.checkOut(parking_ticket_vehicle_3)
        exit_panel.checkOut(parking_ticket_vehicle_4)
        self.assertEqual(parking_ticket_vehicle_3.getAmount(), hourly_cost.getHourlyCost(parking_spot_type=ParkingSpotType.COMPACT))
        self.assertEqual(parking_ticket_vehicle_4.getAmount(), hourly_cost.getHourlyCost(parking_spot_type=ParkingSpotType.LARGE))
        
        parking_ticket_vehicle_5 = entry_panel.getParkingTicket(vehicle_5)
        parking_ticket_vehicle_6 = entry_panel.getParkingTicket(vehicle_6)
        
        self.assertNotEqual(parking_ticket_vehicle_5, 0)
        self.assertNotEqual(parking_ticket_vehicle_6, 0)   

if __name__ == "__main__": 
    unittest.main()