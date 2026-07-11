from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class VehicleBase(BaseModel):
    plate_number: str = Field(..., min_length=2, max_length=20)
    vehicle_type: str = Field(..., min_length=2, max_length=50)
    brand: Optional[str] = None
    color: Optional[str] = None
    owner_name: Optional[str] = None


class VehicleCreate(VehicleBase):
    pass


class VehicleUpdate(BaseModel):
    plate_number: Optional[str] = Field(default=None, min_length=2, max_length=20)
    vehicle_type: Optional[str] = Field(default=None, min_length=2, max_length=50)
    brand: Optional[str] = None
    color: Optional[str] = None
    owner_name: Optional[str] = None


class VehicleRead(VehicleBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime


class ParkingFeeBase(BaseModel):
    vehicle_type: str = Field(..., min_length=2, max_length=50)
    base_fee: Decimal = Field(..., ge=0)
    fee_rule: str = Field(..., min_length=2, max_length=255)
    unit: str = Field(default="per_entry")
    effective_from: Optional[datetime] = None
    effective_to: Optional[datetime] = None
    is_active: bool = True


class ParkingFeeCreate(ParkingFeeBase):
    pass


class ParkingFeeRead(ParkingFeeBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime


class CheckInRequest(BaseModel):
    plate_raw: str = Field(..., min_length=2, max_length=50)
    vehicle_type: str = Field(..., min_length=2, max_length=50)
    parking_lot_id: Optional[int] = None
    entry_image_path: Optional[str] = None
    notes: Optional[str] = None


class CheckOutRequest(BaseModel):
    plate_raw: str = Field(..., min_length=2, max_length=50)
    exit_image_path: Optional[str] = None
    notes: Optional[str] = None


class ParkingSessionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    vehicle_id: int
    parking_lot_id: int
    parking_fee_id: int
    plate_raw: Optional[str] = None
    plate_normalized: str
    vehicle_type_snapshot: str
    status: str
    check_in_time: datetime
    check_out_time: Optional[datetime] = None
    duration_minutes: int
    total_fee: Decimal
    entry_image_path: Optional[str] = None
    exit_image_path: Optional[str] = None
    notes: Optional[str] = None
    created_at: datetime
    updated_at: datetime


class DashboardSummaryRead(BaseModel):
    active_sessions: int
    total_sessions_today: int
    total_revenue_today: Decimal
    motorbike_count: int
    car_count: int
    other_vehicle_count: int
