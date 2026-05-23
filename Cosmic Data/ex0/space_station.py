from datetime import datetime
import sys

try:
    from pydantic import BaseModel, Field, ValidationError
except ImportError:
    print("Pydantic library is not installed. Please install it using 'pip install pydantic' and try again.")
    sys.exit(1)
class SpaceStation(BaseModel):
    
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str| None = Field(None, max_length=200)

def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.2,
            last_maintenance="2024-05-01T10:00:00Z",
            is_operational=True,
            notes="Operational"
        )
    except ValidationError as e:
        print(f"Error occurred: {e}")
    else:
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        print(f"Status: {station.notes}")
        print("========================================")
    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="ISS002",
            name="International Space Station",
            crew_size=25,
            power_level=85.5,
            oxygen_level=92.2,
            last_maintenance="2024-05-01T10:00:00Z"
        )
    except ValidationError as e:
        print(e.errors()[0]['msg'])

if __name__ == "__main__":
    main()
