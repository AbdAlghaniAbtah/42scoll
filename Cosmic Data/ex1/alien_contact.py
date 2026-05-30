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
    model_config = {'validate_assignment': True}

    @model_validator(mode='after')
    def check(self):
        for i, j in enumerate("AC"):
            if j not in self.contact_id[i]:
                raise ValidationError("contact_id must contain 'A' and 'C'")
        
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
            
        if self.contact_type == ContactType.telepathic and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")
            
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError("Strong signals (> 7.0) should include received messages")
            
        return self
        
            
def main():
    print("Alien Contact Log Validation")
    print("======================================")

    try:
        valid_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=False
        )
        print("Valid contact report:")
        print(f"ID: {valid_contact.contact_id}")
        print(f"Type: {valid_contact.contact_type}")
        print(f"Location: {valid_contact.location}")
        print(f"Signal: {valid_contact.signal_strength}/10")
        print(f"Duration: {valid_contact.duration_minutes} minutes")
        print(f"Witnesses: {valid_contact.witness_count}")
        print(f"Message: '{valid_contact.message_received}'")
    except ValidationError as e:
        print(f"Unexpected validation error: {e}")

    print("======================================")


    print("Expected validation error:")
    try:
        AlienContact(
            contact_id="AC_INVALID",
            timestamp=datetime.now(),
            location="Moon Base",
            contact_type=ContactType.telepathic,
            signal_strength=5.0,
            duration_minutes=10,
            witness_count=1,
            is_verified=False
        )
    except ValidationError as e:

        for error in e.errors():
            print(error['msg'].replace("Value error, ", ""))

if __name__ == "__main__":
    main()
