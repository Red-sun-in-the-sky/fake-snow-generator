import json
from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# Define the BusinessService model
class BusinessService(BaseModel):
    Business_Group: str = Field(alias="Business Group")
    Business_Service: str = Field(alias="Business Service")

# Load the JSON file into memory on app startup
with open("bs.json") as f:
    business_services = json.load(f)

# Route to get all unique Business Groups
@app.get("/az/business_groups", response_model=List[str])
def get_business_groups() -> List[str]:
    business_groups = list(set(bs["Business Group"] for bs in business_services))
    return business_groups

# Route to get all Business Services
@app.get("/az/business_services", response_model=List[BusinessService])
def get_business_services() -> List[BusinessService]:
    return business_services

# Route to get Business Services by a specific Business Group
@app.get("/az/business_services/{business_group}", response_model=List[BusinessService])
def get_business_services_by_group(business_group: str) -> List[BusinessService]:
    filtered_services = [bs for bs in business_services if bs["Business Group"] == business_group]
    return filtered_services
