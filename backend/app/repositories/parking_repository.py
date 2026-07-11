from datetime import datetime
from decimal import Decimal
from typing import Iterable, Optional

from sqlalchemy import and_, func, select
from sqlalchemy.orm import Session

from app.infrastructure import models


class ParkingRepository:
    def __init__(self, db: Session):
        self.db = db

    # Vehicle
    def create_vehicle(self, *, plate_number: str, vehicle_type: str, brand: str | None = None, color: str | None = None, owner_name: str | None = None):
        vehicle = models.Vehicle(
            plate_number=plate_number,
            vehicle_type=vehicle_type,
            brand=brand,
            color=color,
            owner_name=owner_name,
        )
        self.db.add(vehicle)
        self.db.flush()
        return vehicle

    def list_vehicles(self, search: str | None = None, vehicle_type: str | None = None):
        query = select(models.Vehicle).order_by(models.Vehicle.created_at.desc())
        if search:
            query = query.where(models.Vehicle.plate_number.contains(search))
        if vehicle_type:
            query = query.where(models.Vehicle.vehicle_type == vehicle_type)
        return list(self.db.scalars(query).all())

    def get_vehicle(self, vehicle_id: int):
        return self.db.get(models.Vehicle, vehicle_id)

    def get_vehicle_by_plate(self, plate_number: str):
        query = select(models.Vehicle).where(models.Vehicle.plate_number == plate_number)
        return self.db.scalar(query)

    def update_vehicle(self, vehicle: models.Vehicle, **changes):
        for field, value in changes.items():
            if value is not None:
                setattr(vehicle, field, value)
        self.db.flush()
        return vehicle

    def delete_vehicle(self, vehicle: models.Vehicle):
        self.db.delete(vehicle)

    # Fee
    def create_fee(self, **data):
        fee = models.ParkingFee(**data)
        self.db.add(fee)
        self.db.flush()
        return fee

    def list_fees(self, active_only: bool = False):
        query = select(models.ParkingFee).order_by(models.ParkingFee.created_at.desc())
        if active_only:
            query = query.where(models.ParkingFee.is_active.is_(True))
        return list(self.db.scalars(query).all())

    def get_active_fee_for_vehicle_type(self, vehicle_type: str):
        query = (
            select(models.ParkingFee)
            .where(models.ParkingFee.vehicle_type == vehicle_type)
            .where(models.ParkingFee.is_active.is_(True))
            .order_by(models.ParkingFee.created_at.desc())
        )
        return self.db.scalar(query)

    # Parking lot
    def get_default_parking_lot(self):
        query = select(models.ParkingLot).where(models.ParkingLot.is_active.is_(True)).order_by(models.ParkingLot.id.asc())
        return self.db.scalar(query)

    def create_parking_lot(self, **data):
        lot = models.ParkingLot(**data)
        self.db.add(lot)
        self.db.flush()
        return lot

    # Session
    def get_active_session_by_vehicle_id(self, vehicle_id: int):
        query = select(models.ParkingSession).where(
            and_(models.ParkingSession.vehicle_id == vehicle_id, models.ParkingSession.status == "active")
        )
        return self.db.scalar(query)

    def list_active_sessions(self):
        query = select(models.ParkingSession).where(models.ParkingSession.status == "active").order_by(models.ParkingSession.check_in_time.desc())
        return list(self.db.scalars(query).all())

    def list_history(self, limit: int = 100):
        query = select(models.ParkingSession).order_by(models.ParkingSession.check_in_time.desc()).limit(limit)
        return list(self.db.scalars(query).all())

    def create_session(self, **data):
        session = models.ParkingSession(**data)
        self.db.add(session)
        self.db.flush()
        return session

    def close_session(self, session: models.ParkingSession, *, check_out_time: datetime, exit_image_path: str | None, duration_minutes: int, total_fee: Decimal, notes: str | None = None):
        session.check_out_time = check_out_time
        session.exit_image_path = exit_image_path
        session.duration_minutes = duration_minutes
        session.total_fee = total_fee
        session.notes = notes or session.notes
        session.status = "closed"
        self.db.flush()
        return session

    def get_session_by_plate(self, plate_number: str):
        query = (
            select(models.ParkingSession)
            .where(models.ParkingSession.plate_normalized == plate_number)
            .order_by(models.ParkingSession.check_in_time.desc())
        )
        return self.db.scalar(query)

    def count_active_sessions(self) -> int:
        query = select(func.count()).select_from(models.ParkingSession).where(models.ParkingSession.status == "active")
        return int(self.db.scalar(query) or 0)

    def count_sessions_today(self) -> int:
        today = datetime.utcnow().date()
        query = select(func.count()).select_from(models.ParkingSession).where(func.date(models.ParkingSession.check_in_time) == today)
        return int(self.db.scalar(query) or 0)

    def revenue_today(self):
        today = datetime.utcnow().date()
        query = select(func.coalesce(func.sum(models.ParkingSession.total_fee), 0)).where(
            and_(models.ParkingSession.status == "closed", func.date(models.ParkingSession.check_out_time) == today)
        )
        return Decimal(str(self.db.scalar(query) or 0))

    def count_vehicles_by_type(self, vehicle_type: str) -> int:
        query = select(func.count()).select_from(models.Vehicle).where(models.Vehicle.vehicle_type == vehicle_type)
        return int(self.db.scalar(query) or 0)
