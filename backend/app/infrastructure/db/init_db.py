from sqlalchemy import select

from app.infrastructure.db.base import Base
from app.infrastructure.db.session import SessionLocal, engine
from app.infrastructure import models


def init_db() -> None:
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as db:
        default_lot = db.scalar(select(models.ParkingLot).where(models.ParkingLot.name == "Default Lot"))
        if default_lot is None:
            db.add(models.ParkingLot(name="Default Lot", location="Main", capacity=100, is_active=True))

        car_fee = db.scalar(select(models.ParkingFee).where(models.ParkingFee.vehicle_type == "car"))
        if car_fee is None:
            db.add(
                models.ParkingFee(
                    vehicle_type="car",
                    base_fee=20000,
                    fee_rule="Default car parking fee",
                    unit="per_entry",
                    is_active=True,
                )
            )

        motorbike_fee = db.scalar(select(models.ParkingFee).where(models.ParkingFee.vehicle_type == "motorbike"))
        if motorbike_fee is None:
            db.add(
                models.ParkingFee(
                    vehicle_type="motorbike",
                    base_fee=10000,
                    fee_rule="Default motorbike parking fee",
                    unit="per_entry",
                    is_active=True,
                )
            )

        db.commit()
