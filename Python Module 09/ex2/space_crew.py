from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
import datetime
from typing import List, Any


class Rank(Enum):

    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):

    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime.datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_rules(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        has_leader = any(
            m.rank in (Rank.COMMANDER, Rank.CAPTAIN) for m in self.crew
        )
        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )
        if self.duration_days > 365:
            exp_count = sum(
                1 for m in self.crew if m.years_experience >= 5
            )
            if exp_count / len(self.crew) < 0.5:
                raise ValueError(
                    "Long mission (> 365 days) need 50% experienced crew"
                )
        if any(not m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("========================================")

    valid_data: dict[str, Any] = {
        "mission_id": "M2026_MARS",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "launch_date": "2026-06-19T08:00:00",
        "duration_days": 900,
        "budget_millions": 2500.0,
        "crew": [
            {
                "member_id": "C01",
                "name": "Sarah Connor",
                "rank": "commander",
                "age": 35,
                "specialization": "Mission Command",
                "years_experience": 10,
            },
            {
                "member_id": "C02",
                "name": "John Smith",
                "rank": "lieutenant",
                "age": 28,
                "specialization": "Navigation",
                "years_experience": 4,
            }
        ]
    }

    print("Valid mission created:")
    mission = SpaceMission.model_validate(valid_data)
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days}")
    print(f"Budget: {mission.budget_millions}")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for m in mission.crew:
        print(f" {m.name} ({m.rank.value}) {m.specialization}")

    print("========================================")
    print("Expected validation error:")
    try:
        invalid_data = valid_data.copy()
        invalid_data["crew"] = [valid_data["crew"][1]]
        SpaceMission.model_validate(invalid_data)
    except ValidationError as err:
        errors_list: Any = err.errors()
        for error in errors_list:
            msg = error["msg"]
            if msg.startswith("Value error, "):
                msg = msg.replace("Value error, ", "")
            print(f"{msg}")


if __name__ == "__main__":
    main()
