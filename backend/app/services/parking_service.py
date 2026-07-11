from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from decimal import Decimal
from math import ceil

from ai.utils.plate_utils import is_valid_plate, normalize_plate

from app.domain.exceptions import ConflictError, NotFoundError, ValidationError
from app.infrastructure import models
from app.schemas.parking import (
    CheckInRequest,
    CheckOutRequest,
    DashboardSummaryRead,
    ParkingFeeCreate,
    ParkingFeeRead,
    ParkingSessionRead,
    VehicleCreate,
    VehicleRead,
    VehicleUpdate,
)


@dataclass
class ParkingService:
    repository: any

    def create_vehicle(self, payload: VehicleCreate):
        plate_number = normalize_plate(payload.plate_number)
        if not is_valid_plate(plate_number):
            raise ValidationError("Invalid plate number")
        existing = self.repository.get_vehicle_by_plate(plate_number)
        if existing:
            raise ConflictError("Vehicle already exists")
        vehicle = self.repository.create_vehicle(
            plate_number=plate_number,
            vehicle_type=payload.vehicle_type,
            brand=payload.brand,
            color=payload.color,
            owner_name=payload.owner_name,
        )
        return vehicle

    def list_vehicles(self, search: str | None = None, vehicle_type: str | None = None):
        return self.repository.list_vehicles(search=search, vehicle_type=vehicle_type)

    def update_vehicle(self, vehicle_id: int, payload: VehicleUpdate):
        vehicle = self.repository.get_vehicle(vehicle_id)
        if not vehicle:
            raise NotFoundError("Vehicle not found")
        changes = payload.model_dump(exclude_unset=True)
        if "plate_number" in changes:
            changes["plate_number"] = normalize_plate(changes["plate_number"])
            if not is_valid_plate(changes["plate_number"]):
                raise ValidationError("Invalid plate number")
        return self.repository.update_vehicle(vehicle, **changes)

    def delete_vehicle(self, vehicle_id: int):
        vehicle = self.repository.get_vehicle(vehicle_id)
        if not vehicle:
            raise NotFoundError("Vehicle not found")
        self.repository.delete_vehicle(vehicle)
        return vehicle

    def create_fee(self, payload: ParkingFeeCreate):
        fee = self.repository.create_fee(**payload.model_dump())
        return fee

    def list_fees(self, active_only: bool = False):
        return self.repository.list_fees(active_only=active_only)

    def _resolve_fee(self, vehicle_type: str):
        fee = self.repository.get_active_fee_for_vehicle_type(vehicle_type)
        if fee:
            return fee
        default_fee = Decimal("20000") if vehicle_type.lower() in {"car", "truck"} else Decimal("10000")
        return models.ParkingFee(
            vehicle_type=vehicle_type,
            base_fee=default_fee,
            fee_rule="default fallback",
            unit="per_entry",
            is_active=True,
        )

    def check_in(self, payload: CheckInRequest):
        plate_normalized = normalize_plate(payload.plate_raw)
        if not is_valid_plate(plate_normalized):
            raise ValidationError("Invalid plate number")

        vehicle = self.repository.get_vehicle_by_plate(plate_normalized)
        if vehicle is None:
            vehicle = self.repository.create_vehicle(
                plate_number=plate_normalized,
                vehicle_type=payload.vehicle_type,
            )

        active_session = self.repository.get_active_session_by_vehicle_id(vehicle.id)
        if active_session:
            raise ConflictError("Vehicle already has an active session")

        parking_lot = self.repository.get_default_parking_lot()
        if parking_lot is None:
            parking_lot = self.repository.create_parking_lot(name="Default Lot", location="Main", capacity=100, is_active=True)

        parking_fee = self._resolve_fee(payload.vehicle_type)
        if getattr(parking_fee, "id", None) is None:
            parking_fee = self.repository.create_fee(
                vehicle_type=payload.vehicle_type,
                base_fee=parking_fee.base_fee,
                fee_rule=parking_fee.fee_rule,
                unit=parking_fee.unit,
                is_active=True,
            )

        session = self.repository.create_session(
            vehicle_id=vehicle.id,
            parking_lot_id=parking_lot.id,
            parking_fee_id=parking_fee.id,
            plate_raw=payload.plate_raw,
            plate_normalized=plate_normalized,
            vehicle_type_snapshot=payload.vehicle_type,
            entry_image_path=payload.entry_image_path,
            notes=payload.notes,
            status="active",
        )
        return session

    def _calc_duration_and_fee(self, check_in_time: datetime, check_out_time: datetime, fee: models.ParkingFee):
        delta = check_out_time - check_in_time
        duration_minutes = max(0, int(delta.total_seconds() // 60))
        if fee.unit == "per_hour":
            hours = max(1, ceil(duration_minutes / 60))
            total_fee = Decimal(str(fee.base_fee)) * Decimal(hours)
        elif fee.unit == "per_minute":
            total_fee = Decimal(str(fee.base_fee)) * Decimal(duration_minutes)
        else:
            total_fee = Decimal(str(fee.base_fee))
        return duration_minutes, total_fee

    def check_out(self, payload: CheckOutRequest):
        plate_normalized = normalize_plate(payload.plate_raw)
        if not is_valid_plate(plate_normalized):
            raise ValidationError("Invalid plate number")

        session = self.repository.get_session_by_plate(plate_normalized)
        if not session or session.status != "active":
            raise NotFoundError("Active session not found")

        check_out_time = datetime.utcnow()
        fee = session.parking_fee or self.repository.get_active_fee_for_vehicle_type(session.vehicle_type_snapshot)
        if fee is None:
            raise NotFoundError("Parking fee not found")

        duration_minutes, total_fee = self._calc_duration_and_fee(session.check_in_time, check_out_time, fee)
        updated = self.repository.close_session(
            session,
            check_out_time=check_out_time,
            exit_image_path=payload.exit_image_path,
            duration_minutes=duration_minutes,
            total_fee=total_fee,
            notes=payload.notes,
        )
        return updated

    def list_active_sessions(self):
        return self.repository.list_active_sessions()

    def list_history(self, limit: int = 100):
        return self.repository.list_history(limit=limit)

    def dashboard_summary(self):
        return DashboardSummaryRead(
            active_sessions=self.repository.count_active_sessions(),
            total_sessions_today=self.repository.count_sessions_today(),
            total_revenue_today=self.repository.revenue_today(),
            motorbike_count=self.repository.count_vehicles_by_type("motorbike"),
            car_count=self.repository.count_vehicles_by_type("car"),
            other_vehicle_count=self.repository.count_vehicles_by_type("other"),
        )
