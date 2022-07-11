"""FastAPI models."""
from pydantic import BaseModel
from typing import List

class HealthCheck(BaseModel):
    """Health check response model."""
    status: int
    api_version: str

class AvailableUnits(BaseModel):
    """AvailableUnits model for a response."""

    status: int
    message: str
    vehicle_ids: List[int]

class UnitLocation(BaseModel):
    """Unit location model for a response."""

    status: int
    message: str
    unit_id: int
    position_latitude: float
    position_longitude: float

class AvailableMayors(BaseModel):
    """Available mayors model for a response."""

    status: int
    message: str
    mayors: List[str]