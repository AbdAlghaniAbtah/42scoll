from datetime import datetime
import enum
from typing import List
import sys


try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except ImportError:
    print("Pydantic library is not installed. Please install it using 'pip install pydantic' and try again.")
    sys.exit(1)
    
class DefineCrewRole(enum.Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: DefineCrewRole
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True
    model_config = {'validate_assignment': True}

class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_items=3, max_items=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_items=1, max_items=10)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=100000.0)
    model_config = {'validate_assignment': True}

    @model_validator(mode='after')
    def check(self):
        if self.mission_id[0] != "M":
            raise ValueError("mission_id must start with 'M'")
        if len(self.crew) < 1:
            raise ValueError("Mission must have at least one crew member")
        if self.duration_days > 365:
            j = 0
            for i in self.crew:
                if i.years_experience > 5:
                    j += 1
            for _ in self.crew:
                if j < len(self.crew) / 2:
                    raise ValueError("Long missions (> 365 days) require at least half the crew to have > 5 years experience")
        for i in self.crew:
            if i.is_active == False:
                raise ValueError("Inactive crew members cannot be assigned to active missions")
        return self
    
def main():
    print("Space Mission Crew Validation")
    print("=========================================")

    try:
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2025, 5, 20),
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(member_id="C01", name="Sarah Connor", rank=DefineCrewRole.commander, age=40, specialization="Mission Command", years_experience=10),
                CrewMember(member_id="C02", name="John Smith", rank=DefineCrewRole.lieutenant, age=35, specialization="Navigation", years_experience=6),
                CrewMember(member_id="C03", name="Alice Johnson", rank=DefineCrewRole.officer, age=30, specialization="Engineering", years_experience=2)
            ]
        )
        print("Valid mission created:")
        print(f"Mission: {valid_mission.mission_name}")
        print(f"ID: {valid_mission.mission_id}")
        print(f"Destination: {valid_mission.destination}")
        print(f"Duration: {valid_mission.duration_days} days")
        print(f"Budget: ${valid_mission.budget_millions}M")
        print(f"Crew size: {len(valid_mission.crew)}")
        print("Crew members:")
        for member in valid_mission.crew:
            print(f"- {member.name} ({member.rank.value}) - {member.specialization}")
    except ValidationError as e:
        print(f"Unexpected error: {e}")

    print("=========================================")

    print("Expected validation error:")
    try:
        SpaceMission(
            mission_id="M12345",
            mission_name="Ghost Mission",
            destination="Void",
            launch_date=datetime.now(),
            duration_days=100,
            budget_millions=100.0,
            crew=[
                CrewMember(member_id="C99", name="Newbie", rank=DefineCrewRole.cadet, age=20, specialization="Training", years_experience=0)
            ]
        )
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'].replace("Value error, ", ""))

if __name__ == "__main__":
    main()