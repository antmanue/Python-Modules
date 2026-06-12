from pydantic import BaseModel, Field
import datetime
from typing import Optional

class SpaceStation(BaseModel):
    
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime.datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)

def main() -> None:
    print("Space Station Data Validation")

    valid_station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2026-06-11T12:00:00",
    )

    print("Valid station created:")
    print(f"ID: {valid_station.station_id}")
    print(f"Name: {valid_station.name}")
    print(f"Crew: {valid_station.crew_size}")
    print(f"Last Maintenance: {valid_station.last_maintenance}")
    print(f"Power: {valid_station.power_level9}")
    print(f"Oxygen: {valid_station.oxygen_level}")
    print(f"Status: {valid_station.is_operational}")

