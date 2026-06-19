from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
import datetime
from typing import Optional


class ContactType(Enum):

    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime.datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate_contact_rules(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if (
           self.contact_type == ContactType.PHYSICAL
           and not self.is_verified):
            raise ValueError(
                "Physical contact reports must be verified"
                )
        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
                )
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0)"
                "should include received messages"
            )
        return self


def main() -> None:
    print("Alien Contact Log Validaton")
    print("========================================")

    valid_data = {
        "contact_id": "AC_2024_001",
        "timestamp": "2026-06-18T19:00:00",
        "location": "Area 51, Neveda",
        "contact_type": "radio",
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 5,
        "message_received": "Greatings from Zeta Reticuli"
    }

    print("Valid contact report:")
    report = AlienContact.model_validate(valid_data)

    print(f"ID: {report.contact_id}")
    print(f"Type: {report.contact_type.value}")
    print(f"Location: {report.location}")
    print(f"Signal: {report.signal_strength}/10")
    print(f"Duration: {report.duration_minutes} minutes")
    print(f"Witnesses: {report.witness_count}")
    print(f"Message: '{report.message_received}'")

    print("========================================")
    print("Expected validation error:")
    try:
        invalid_data = valid_data.copy()
        invalid_data["contact_type"] = "telepathic"
        invalid_data["witness_count"] = 1

        AlienContact.model_validate(invalid_data)

    except ValidationError as err:
        for error in err.errors():
            msg = error["msg"]
            if msg.startswith("Value error, "):
                msg = msg.replace("Value error, ", "")
            print(f"{msg}")


if __name__ == "__main__":
    main()
