from urllib import response
from fastapi import FastAPI, Request, Response, status, Depends
from sqlalchemy.orm import Session
from loguru import logger
from app.api.db.database import SessionLocal
from app.api.db import db_service
from app.api import models
from app.api.models import HealthCheck

API_VERSION = "v0.0.1"

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/status", response_model=HealthCheck)
@app.get("/status/", response_model=HealthCheck)
def health_check(request: Request):
    """
    Health check of the API.

    Keyword Arguments:
        request {Request} -- The FastAPI Request object associated with the current call

    Returns:
        models.HealthCheck -- JSON dict HealthCheck
    """
    response = {
        "status": 200,
        "api_version": API_VERSION
    }
    return response

@app.get("/available-units", response_model=models.AvailableUnits)
@app.get("/available-units/", response_model=models.AvailableUnits)
def available_units(response: Response, db: Session = Depends(get_db)):
    """Get available units.

    param response Response: response object
    param db Session: database object
    return response models.AvailableUnits: AvailableUnits model (JSON).
    """

    result = db_service.get_available_units(db)
    
    if len(result) == 0:
        body_response = {
            "status": status.HTTP_404_NOT_FOUND,
            "message": "There are not units available",
            "vehicle_ids": []
        }
        
        response.status_code = status.HTTP_404_NOT_FOUND
        return body_response

    mb_units = [int(unit.vehicle_id) for unit in result]
    
    body_response = {
            "status": status.HTTP_200_OK,
            "message": f"There are {len(mb_units)} MB units available",
            "vehicle_ids": mb_units
        }
    
    return body_response

@app.get("/unit-location/", response_model=models.UnitLocation)
@app.get("/unit-location/{unit_id}", response_model=models.UnitLocation)
@app.get("/unit-location/{unit_id}/", response_model=models.UnitLocation)
def unit_location(response: Response, unit_id: str, db: Session = Depends(get_db)):
    """Get unit location by ID.

    param response Response: response object
    param unit_id int: MB unit identifier
    param db Session: database object
    return response models.UnitLocation: UnitLocation model (JSON).
    """

    if not unit_id:
        body_response = {
            "status": status.HTTP_400_BAD_REQUEST,
            "message": f"Bad request, unit identifier field required",
            "unit_id": 0,
            "position_latitude": 0.0,
            "position_longitude": 0.0
        }

        response.status_code = status.HTTP_400_BAD_REQUEST
        return body_response


    result = db_service.get_location_by_id(db, unit_id)
    
    if not result:
        body_response = {
            "status": status.HTTP_404_NOT_FOUND,
            "message": f"There is not a unit for this id",
            "unit_id": unit_id,
            "position_latitude": 0.0,
            "position_longitude": 0.0
        }
        
        response.status_code = status.HTTP_404_NOT_FOUND
        return body_response

    body_response = {
            "status": status.HTTP_200_OK,
            "message": f"Location getted successfully",
            "unit_id": unit_id,
            "position_latitude": float(result.position_latitude),
            "position_longitude": float(result.position_longitude)
        }
    
    return body_response


@app.get("/available-mayors", response_model=models.AvailableMayors)
@app.get("/available-mayors/", response_model=models.AvailableMayors)
def available_mayors(response: Response, db: Session = Depends(get_db)):
    """Get available mayors.

    param response Response: response object
    param db Session: database object
    return response models.AvailableUnits: AvailableUnits model (JSON).
    """

    result = db_service.get_mayors(db)
    
    if len(result) == 0:
        body_response = {
            "status": status.HTTP_404_NOT_FOUND,
            "message": "There are not mayors available",
            "mayors": []
        }
        
        response.status_code = status.HTTP_404_NOT_FOUND
        return body_response

    mayors = [str(mayor.alcaldia) for mayor in result]
    
    body_response = {
            "status": status.HTTP_200_OK,
            "message": f"There is/are {len(mayors)} mayor/s available",
            "mayors": mayors
        }
    
    return body_response

@app.get("/units-by-mayor/", response_model=models.AvailableUnits)
@app.get("/units-by-mayor/{mayor}", response_model=models.AvailableUnits)
@app.get("/units-by-mayor/{mayor}/", response_model=models.AvailableUnits)
def units_by_mayor(response: Response, mayor: str, db: Session = Depends(get_db)):
    """Get available units in a specyfic location.

    param response Response: response object
    param mayor str: mayor name
    param db Session: database object
    return response models.AvailableUnits: AvailableUnits model (JSON).
    """

    result = db_service.get_units_by_mayor(db, mayor)

    if len(result) == 0:
        body_response = {
            "status": status.HTTP_404_NOT_FOUND,
            "message": f"There are not units available in {mayor}",
            "vehicle_ids": []
        }

        response.status_code = status.HTTP_404_NOT_FOUND
        return body_response

    mb_units = [int(unit.vehicle_id) for unit in result]

    body_response = {
            "status": status.HTTP_200_OK,
            "message": f"There is/are {len(mb_units)} unit/s available in {mayor}",
            "vehicle_ids": mb_units
        }

    return body_response