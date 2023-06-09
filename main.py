import json
import threading
import httpx
from typing import List, Optional
from fastapi import FastAPI
from models.ticket import Ticket
from models.business_service import BusinessService
from generator.ticket_generator import TicketGenerator

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    # Init tickets generator execution on the background
    threading.Thread(target=ticket_generator.run, daemon=True).start()

async def post_updated_tickets(tickets):
    url = "http://0.0.0.0:8080/tickets"  # Reemplaza esto con la URL de tu endpoint en az-watch
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=[ticket.dict() for ticket in tickets])

    if response.status_code != 200:
        print(f"Error al enviar los tickets actualizados a az-watch: {response.text}")


# Load the JSON file into memory on app startup
with open("resources/bs.json") as f:
    business_services = json.load(f)

# Extract the list of business service names
business_service_names = [
    item for group in business_services for item in group["Business Services"]
]

# Create an instance of TicketGenerator with the business service names
ticket_generator = TicketGenerator(business_services=business_service_names, callback=post_updated_tickets)


@app.on_event("startup")
async def startup_event():
    # Init tickets generator execution on the background
    threading.Thread(target=ticket_generator.run, daemon=True).start()

# Route to get all tickets
@app.get(
    "/az/tickets/",
    response_model=List[Ticket],
)
def get_all_tickets() -> List[Ticket]:
    # Load the tickets JSON file into memory when the endpoint is called
    with open("resources/tickets.json") as f:
        tickets_data = json.load(f)

    # Convert the JSON data to Ticket objects
    tickets = [Ticket(**ticket) for ticket in tickets_data]

    return tickets