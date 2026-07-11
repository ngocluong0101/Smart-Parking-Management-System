from fastapi import APIRouter, Depends

from app.core.dependencies import get_parking_service
from app.schemas.parking import ParkingFeeCreate, ParkingFeeRead
from app.services.parking_service import ParkingService

router = APIRouter(prefix="/parking-fees")


@router.get("", response_model=list[ParkingFeeRead])
def list_fees(service: ParkingService = Depends(get_parking_service)):
    return service.list_fees(active_only=False)


@router.post("", response_model=ParkingFeeRead)
def create_fee(payload: ParkingFeeCreate, service: ParkingService = Depends(get_parking_service)):
    return service.create_fee(payload)
