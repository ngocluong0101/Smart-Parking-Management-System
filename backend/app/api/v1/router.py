from fastapi import APIRouter

from app.api.v1.health import router as health_router
from app.api.v1.ai import router as ai_router

api_router = APIRouter()
api_router.include_router(health_router, tags=["Health"])
api_router.include_router(ai_router, tags=["AI"])
