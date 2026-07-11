from fastapi import APIRouter

from app.api.v1.dashboard import router as dashboard_router
from app.api.v1.fees import router as fees_router
from app.api.v1.health import router as health_router
from app.api.v1.ai import router as ai_router
from app.api.v1.parking import router as parking_router
from app.api.v1.vehicles import router as vehicles_router

api_router = APIRouter()
api_router.include_router(health_router, tags=["Health"])
api_router.include_router(ai_router, tags=["AI"])
api_router.include_router(vehicles_router, tags=["Vehicles"])
api_router.include_router(parking_router, tags=["Parking Sessions"])
api_router.include_router(fees_router, tags=["Parking Fees"])
api_router.include_router(dashboard_router, tags=["Dashboard"])
