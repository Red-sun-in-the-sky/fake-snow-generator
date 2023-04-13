import json
import time
import random
from typing import List
from models.ticket import Ticket


class TicketGenerator:
    def __init__(
        self,
        max_tickets: int = 30,
        tickets_file_path: str = "resources/tickets.json",
        business_services: List[str] = None,
    ):
        self.max_tickets = max_tickets
        self.tickets_file_path = tickets_file_path
        self.business_services = business_services or []
        self.tickets = self.load_tickets()
        self.update_interval = 15

    def load_tickets(self) -> List[Ticket]:
        try:
            with open(self.tickets_file_path, "r") as file:
                tickets_data = json.load(file)
            return [Ticket(**ticket_data) for ticket_data in tickets_data]
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def generate_ticket(self) -> Ticket:
        incident_number = f"INC{random.randint(100000, 999999)}"
        business_service = random.choice(self.business_services)
        priority = random.choice(["P1", "P2", "P3", "P4"])
        description = "Sample description"
        status = "New"
        new_ticket = Ticket(
            incident_number=incident_number,
            Business_Service=business_service,
            priority=priority,
            description=description,
            status=status,
        )
        return new_ticket

    def update_ticket_status(self, ticket: Ticket) -> Ticket:
        status_sequence = [
            "New",
            "Assigned",
            "In Progress",
            "Resolved",
            "Closed",
        ]
        current_status_index = status_sequence.index(ticket.status)
        if current_status_index < len(status_sequence) - 1:
            next_status_index = random.randint(
                current_status_index + 1,
                min(current_status_index + 2, len(status_sequence) - 1),
            )
            ticket.status = status_sequence[next_status_index]
            ticket.system_status = ticket.assign_system_status()
            if ticket.status in ["Resolved", "Closed"]:
                ticket.resolved_closed_updates += 1
        return ticket

    def run(self):
        while True:
            # Update existing tickets
            self.tickets = [
                self.update_ticket_status(ticket) for ticket in self.tickets
            ]
            # Remove tickets that meet the condition
            self.tickets = [
                ticket for ticket in self.tickets if ticket.resolved_closed_updates < 3
            ]
            # Create new tickets if necessary
            if len(self.tickets) < self.max_tickets:
                new_ticket = self.generate_ticket()
                self.tickets.append(new_ticket)

            # Save the updated tickets to the JSON file
            with open(self.tickets_file_path, "w") as file:
                json.dump(
                    [ticket.dict() for ticket in self.tickets], file, indent=2
                )

            # Wait before updating the tickets again
            time.sleep(self.update_interval)
