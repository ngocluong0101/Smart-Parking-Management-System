from fastapi import APIRouter, Depends, Query

from app.core.dependencies import get_parking_service
from app.schemas.parking import VehicleCreate, VehicleRead, VehicleUpdate
from app.services.parking_service import ParkingService

router = APIRouter(prefix="/vehicles")


@router.post("", response_model=VehicleRead)
def create_vehicle(payload: VehicleCreate, service: ParkingService = Depends(get_parking_service)):
    return service.create_vehicle(payload)


@router.get("", response_model=list[VehicleRead])
def list_vehicles(
    search: str | None = Query(default=None),
    vehicle_type: str | None = Query(default=None),
    service: ParkingService = Depends(get_parking_service),
):
    return service.list_vehicles(search=search, vehicle_type=vehicle_type)


@router.patch("/{vehicle_id}", response_model=VehicleRead)
def update_vehicle(vehicle_id: int, payload: VehicleUpdate, service: ParkingService = Depends(get_parking_service)):
    return service.update_vehicle(vehicle_id, payload)


@router.delete("/{vehicle_id}", response_model=VehicleRead)
def delete_vehicle(vehicle_id: int, service: ParkingService = Depends(get_parking_service)):
    return service.delete_vehicle(vehicle_id)
