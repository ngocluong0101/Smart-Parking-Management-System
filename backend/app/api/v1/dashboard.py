from fastapi import APIRouter, Depends

from app.core.dependencies import get_parking_service
from app.schemas.parking import DashboardSummaryRead
from app.services.parking_service import ParkingService

router = APIRouter(prefix="/dashboard")


@router.get("/summary", response_model=DashboardSummaryRead)
def dashboard_summary(service: ParkingService = Depends(get_parking_service)):
    return service.dashboard_summary()
