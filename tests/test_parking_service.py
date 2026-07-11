from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from decimal import Decimal

import pytest

from app.domain.exceptions import ConflictError, NotFoundError, ValidationError
from app.schemas.parking import CheckInRequest, CheckOutRequest, ParkingFeeCreate, VehicleCreate, VehicleUpdate
from app.services.parking_service import ParkingService


@dataclass
class FakeVehicle:
    id: int
    plate_number: str
    vehicle_type: str
    brand: str | None = None
    color: str | None = None
    owner_name: str | None = None


@dataclass
class FakeFee:
    id: int | None
    vehicle_type: str
    base_fee: Decimal
    fee_rule: str
    unit: str = "per_entry"
    is_active: bool = True


@dataclass
class FakeLot:
    id: int
    name: str = "Default Lot"
    location: str = "Main"
    capacity: int = 100
    is_active: bool = True


@dataclass
class FakeSession:
    id: int
    vehicle_id: int
    parking_lot_id: int
    parking_fee_id: int
    plate_raw: str | None
    plate_normalized: str
    vehicle_type_snapshot: str
    status: str = "active"
    check_in_time: datetime = datetime.utcnow()
    check_out_time: datetime | None = None
    duration_minutes: int = 0
    total_fee: Decimal = Decimal("0")
    entry_image_path: str | None = None
    exit_image_path: str | None = None
    notes: str | None = None
    parking_fee: FakeFee | None = None


class FakeRepository:
    def __init__(self):
        self.vehicle_seq = 1
        self.fee_seq = 1
        self.lot_seq = 1
        self.session_seq = 1
        self.vehicles: dict[str, FakeVehicle] = {}
        self.sessions: list[FakeSession] = []
        self.fees: dict[str, FakeFee] = {
            "car": FakeFee(id=1, vehicle_type="car", base_fee=Decimal("20000"), fee_rule="default"),
            "motorbike": FakeFee(id=2, vehicle_type="motorbike", base_fee=Decimal("10000"), fee_rule="default"),
        }
        self.default_lot = FakeLot(id=1)

    def create_vehicle(self, *, plate_number: str, vehicle_type: str, brand=None, color=None, owner_name=None):
        vehicle = FakeVehicle(self.vehicle_seq, plate_number, vehicle_type, brand, color, owner_name)
        self.vehicles[plate_number] = vehicle
        self.vehicle_seq += 1
        return vehicle

    def list_vehicles(self, search=None, vehicle_type=None):
        return list(self.vehicles.values())

    def get_vehicle(self, vehicle_id: int):
        return next((vehicle for vehicle in self.vehicles.values() if vehicle.id == vehicle_id), None)

    def get_vehicle_by_plate(self, plate_number: str):
        return self.vehicles.get(plate_number)

    def update_vehicle(self, vehicle, **changes):
        for key, value in changes.items():
            setattr(vehicle, key, value)
        return vehicle

    def delete_vehicle(self, vehicle):
        self.vehicles.pop(vehicle.plate_number, None)
        return vehicle

    def create_fee(self, **data):
        fee = FakeFee(id=self.fee_seq, **data)
        self.fees[fee.vehicle_type] = fee
        self.fee_seq += 1
        return fee

    def list_fees(self, active_only=False):
        return list(self.fees.values())

    def get_active_fee_for_vehicle_type(self, vehicle_type: str):
        return self.fees.get(vehicle_type)

    def get_default_parking_lot(self):
        return self.default_lot

    def create_parking_lot(self, **data):
        lot = FakeLot(id=self.lot_seq, **data)
        self.default_lot = lot
        self.lot_seq += 1
        return lot

    def get_active_session_by_vehicle_id(self, vehicle_id: int):
        return next((session for session in self.sessions if session.vehicle_id == vehicle_id and session.status == "active"), None)

    def list_active_sessions(self):
        return [session for session in self.sessions if session.status == "active"]

    def list_history(self, limit: int = 100):
        return self.sessions[:limit]

    def create_session(self, **data):
        fee = self.fees.get(data["vehicle_type_snapshot"])
        session = FakeSession(id=self.session_seq, parking_fee=fee, **data)
        self.sessions.append(session)
        self.session_seq += 1
        return session

    def close_session(self, session, *, check_out_time, exit_image_path, duration_minutes, total_fee, notes=None):
        session.status = "closed"
        session.check_out_time = check_out_time
        session.exit_image_path = exit_image_path
        session.duration_minutes = duration_minutes
        session.total_fee = total_fee
        session.notes = notes
        return session

    def get_session_by_plate(self, plate_number: str):
        for session in reversed(self.sessions):
            if session.plate_normalized == plate_number:
                return session
        return None

    def count_active_sessions(self):
        return len([session for session in self.sessions if session.status == "active"])

    def count_sessions_today(self):
        return len(self.sessions)

    def revenue_today(self):
        return sum((session.total_fee for session in self.sessions if session.status == "closed"), Decimal("0"))

    def count_vehicles_by_type(self, vehicle_type: str):
        return len([vehicle for vehicle in self.vehicles.values() if vehicle.vehicle_type == vehicle_type])


@pytest.fixture()
def service():
    return ParkingService(FakeRepository())


def test_check_in_creates_session(service: ParkingService):
    session = service.check_in(CheckInRequest(plate_raw="29a-12345", vehicle_type="car"))
    assert session.status == "active"
    assert session.plate_normalized == "29A-12345"


def test_check_out_closes_session(service: ParkingService):
    service.check_in(CheckInRequest(plate_raw="29a-12345", vehicle_type="car"))
    closed = service.check_out(CheckOutRequest(plate_raw="29a-12345"))
    assert closed.status == "closed"
    assert closed.total_fee == Decimal("20000")


def test_duplicate_check_in_raises(service: ParkingService):
    service.check_in(CheckInRequest(plate_raw="29a-12345", vehicle_type="car"))
    with pytest.raises(ConflictError):
        service.check_in(CheckInRequest(plate_raw="29a-12345", vehicle_type="car"))


def test_invalid_vehicle_plate_raises(service: ParkingService):
    with pytest.raises(ValidationError):
        service.create_vehicle(VehicleCreate(plate_number="abc", vehicle_type="car"))
