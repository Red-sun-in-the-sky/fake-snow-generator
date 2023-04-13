import random
import string
from pydantic import BaseModel, Field


class Ticket(BaseModel):
    sys_id: str = Field(
        default_factory=lambda: "".join(random.choices(string.hexdigits, k=32)).lower()
    )
    Business_Service: str
    number: str = Field(default_factory=lambda: f"INC{random.randint(100000, 999999)}")
    short_description: str = Field(default_factory=lambda: Ticket.generate_random_description())
    priority: str = Field(default_factory=lambda: f"P{random.randint(1, 4)}")
    status: str
    system_status: str = Field(default_factory=lambda: random.choice(["Yellow", "Red"]))
    resolved_closed_updates: int = 0

    class Config:
        allow_population_by_field_name = True

    def __init__(self, **data):
        super().__init__(**data)
        self.system_status = self.assign_system_status()

    @staticmethod
    def generate_random_description():
        descriptions = [
            "User cannot access email",
            "VPN connection issue",
            "Service is loading slow",
            "Users unable to access to the main repository",
        ]
        return random.choice(descriptions)

    def assign_system_status(self):
        if self.status in ["Resolved", "Closed"]:
            return "Green"
        elif self.priority == "P1":
            return "Red"
        elif self.priority == "P2" or self.status == "In Progress":
            return "Yellow"
        else:
            return "Green"
