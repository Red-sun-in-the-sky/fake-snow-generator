from typing import List
from pydantic import BaseModel, Field


class BusinessService(BaseModel):
    Business_Group: str = Field(alias="Business Group")
    Business_Services: List[str] = Field(alias="Business Services")
