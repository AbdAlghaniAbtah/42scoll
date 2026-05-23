from datetime import datetime
import enum
import sys



try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except ImportError:
    print("Pydantic library is not installed. Please install it using 'pip install pydantic' and try again.")
    sys.exit(1)

class ContactType(enum.Enum):
    radio = "visitor"
    visual = "ambassador"
    physical = "scientist"
    telepathic = "diplomat"
    def __str__(self) -> str:
        return self.value

class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength : float = Field(..., ge=0.0, le=100.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: str | None = Field(None, max_length=500)
    is_verified: bool = False
    @model_validator(mode='after')
    def check(self):
        for i, j in enumerate("AC"):
            if j not in self.contact_id[i]:
                raise ValidationError("contact_id must contain 'A' and 'C'")
        return self
            
def main() -> None:
    x = AlienContact(
        contact_id="AC1234567894",
        timestamp="2024-06-01T12:00:00Z",
        location="Sector 7G",
        contact_type=ContactType.radio,
        signal_strength=75.5,
        duration_minutes=30,
        witness_count=5,
        message_received="We come in peace.",
        is_verified=True
    )
    y = ContactType.radio
    print(y)


if __name__ == "__main__":
    main()