from datetime import date
from pydantic import BaseModel

class AircraftBase(BaseModel):
    registration: str
    type: str
    last_maintenance: date | None = None
    next_maintenance: date | None = None

class AircraftCreate(AircraftBase):
    pass

class Aircraft(AircraftBase):
    id: int

    class Config:
        orm_mode = True
