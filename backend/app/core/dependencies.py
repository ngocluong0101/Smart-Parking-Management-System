from collections.abc import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from app.infrastructure.db.session import get_db
from app.repositories.parking_repository import ParkingRepository
from app.services.parking_service import ParkingService


def get_parking_repository(db: Session = Depends(get_db)) -> ParkingRepository:
    return ParkingRepository(db)


def get_parking_service(repository: ParkingRepository = Depends(get_parking_repository)) -> ParkingService:
    return ParkingService(repository)
