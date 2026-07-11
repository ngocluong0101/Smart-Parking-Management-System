from fastapi import APIRouter, Depends, Query

from app.core.dependencies import get_parking_service
from app.schemas.parking import CheckInRequest, CheckOutRequest, ParkingSessionRead
from app.services.parking_service import ParkingService

router = APIRouter(prefix="/parking-sessions")


@router.post("/check-in", response_model=ParkingSessionRead)
def check_in(payload: CheckInRequest, service: ParkingService = Depends(get_parking_service)):
    return service.check_in(payload)


@router.post("/check-out", response_model=ParkingSessionRead)
def check_out(payload: CheckOutRequest, service: ParkingService = Depends(get_parking_service)):
    return service.check_out(payload)


@router.get("/active", response_model=list[ParkingSessionRead])
def list_active_sessions(service: ParkingService = Depends(get_parking_service)):
    return service.list_active_sessions()


@router.get("/history", response_model=list[ParkingSessionRead])
def list_history(limit: int = Query(default=100, ge=1, le=500), service: ParkingService = Depends(get_parking_service)):
    return service.list_history(limit=limit)
