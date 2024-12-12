- Following References have been used to Write this Parking Lot code: 
- https://medium.com/@madhankumaravelu93/low-level-system-design-parking-lot-design-part-i-7567d510da1d 
- https://medium.com/@madhankumaravelu93/low-level-system-design-parking-lot-design-part-ii-ab5f4efab90 
- https://mermaid.js.org/syntax/classDiagram.html



```mermaid

classDiagram

class ParkingLot{
- instance: ParkingLot
- parkingFloors: Array~ParkingFloor~
- exitPanels: Array~ExitPanel~
- entryPanels: Array~EntryPanel~
+ getInstance(): ParkingLot
+ getListofParkingFloors(): ParkingFloor[]
+ getListofExitPanels(): ExistPanel[]
+ getListofEntryPanels(): EntryPanel[]
+ getParkingSpot(parkingSpotId: string): ParkingSpot | null
}
ParkingLot *-- ParkingFloor: Composition
ParkingLot *-- EntryPanel: Composition
ParkingLot *-- ExitPanel: Composition

class Account{
    - userName: string
    - password: string
}

class Admin{
    + addParkingFloor(parking_floor: ParkingFloor): bool
    + addParkingSpot(parking_floor_id: string, parking_spot: ParkingSpot): null
    + addEntryPanel(entry_panel: EntryPanel): null
    + addExitPanel(exit_panel: ExitPanel): null
}

Account <|-- Admin: Extends
Account <|-- Attendant: Extends

class ParkingFloor{
- parkingFloorId: string
- parkingSpotMap: Map~ParkingSpotType, Array~ParkingSpot~~
- displayBoard: DisplayBoard
+ getParkingFloorId(): string
+ getListOfParkingSpots(): Map<ParkingSpotType, ParkingSpot[]>
+ showDisplayBoard(message: string): Void
+ getAvailableSpot(vehicle: Vehicle): ParkingSpot | null
- getSpotTypeForVehicle(vehicleType: VehicleType): ParkingSpotType
+ getInUseSpotsForVehicleType(vehicleType: VehicleType): ParkingSpot[]
}

 ParkingFloor *-- ParkingSpot: Composition
 ParkingFloor *-- DisplayBoard: Composition
 ParkingFloor ..> ParkingSpotType: Dependency

class EntryPanel{
 - entryPanelId: string
 + getEntryPanelId(): string
 + getParkingTicket(vehicle: Vehicle): ParkingTicket
 - generateParkingTicket(vehicle: Vehicle, floor_id: string, spot_id: string): ParkingTicket
}

class ExitPanel{
 - exitPanelId: string
 + getExitPanelId(): string
 + checkOut(parkingTicket: ParkingTicket): void
 - calculateHours(parkingTicket: ParkingTicket): number
 - calculateAmount(parkingSpotType: ParkingSpotType, duration: float): number
}

class ParkingSpot{
    - parkingSpotId: string
    - isSpotAvailable: bool
    - vehicle: Vehicle
    - parkingSpotType: ParkingSpotType

    + getParkingSpotId(): string
    + isSpotFree(): bool
    + getParkingSpotType(): ParkingSpotType
    + getVehicleDetails(): Vehicle | null
    + assignVehicleToSpot(vehicle: Vehicle): bool
    + vacateVehicleFromSpot(): bool
}
class ParkingSpotType{
    <<enumeration>>
    Disabled
    Compact
    Large
    Motorcycle
    ElectricCar
}
ParkingSpot <|-- CarSpot: Extends
ParkingSpot <|-- DisabledSpot: Extends
ParkingSpot <|-- ElectricCarSpot: Extends
ParkingSpot <|-- MotorCycleSpot: Extends
ParkingSpot ..> ParkingSpotType: Dependency
ParkingSpot --> Vehicle: has

class Vehicle{
- registrationNumber: string
- vehicleType: VehicleType
+ getregistrationNumber(): string
+ getVehicleType(): VehicleType
}

Vehicle <|-- Car: Extends
Vehicle <|-- Truck: Extends
Vehicle <|-- MotorCycle: Extends
Vehicle <|-- ElectricCar: Extends
Vehicle <|-- ElectricCar: Extends
Vehicle ..> VehicleType: Dependency

class VehicleType{
<<enumeration>>
    Car
    MotorCycle
    Truck
    ElectricCar
    Van
}
class ParkingTicket{
- parkingTicketId: string
- vehicleRegistrationId: string
- parkingFloorId: string
- parkingSpotId: string
- vehicleType: VehicleType
- startTime: DateTime
- endTime: DateTime
- amount: number

+ getParkingTicketId(): string
+ getVehicleRegistrationNumber(): string
+ getParkingSpotId(): string
+ getParkingFloorId(): string
+ getVehicleType(): VehicleType
+ setStartTime(startTime: DateTime): self
+ setEndTime(endTime: DateTime): self
+ getStartTime(): datetime
+ getEndTime(): datetime
+ getAmount(): number
+ setAmount(amount: number): self 
}

class DisplayBoard{
diplayMessage(message: string): void
}

class HourlyCost{
- hourlyCosts: Map<ParkingSpotType, number>
+ getHourlyCost(parkingSpotType:ParkingSpotType): number
}

EntryPanel *-- ParkingTicket: Composition
ExitPanel *-- ParkingTicket: Composition
ExitPanel --> HourlyCost: has
ExitPanel *--  Payment: Composition
```