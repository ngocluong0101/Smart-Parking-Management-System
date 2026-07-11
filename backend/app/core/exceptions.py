from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.domain.exceptions import ConflictError, NotFoundError, ParkingError, ValidationError


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(ParkingError)
    async def parking_error_handler(request: Request, exc: ParkingError) -> JSONResponse:
        status_code = 400
        if isinstance(exc, NotFoundError):
            status_code = 404
        elif isinstance(exc, ConflictError):
            status_code = 409
        elif isinstance(exc, ValidationError):
            status_code = 422

        return JSONResponse(
            status_code=status_code,
            content={"success": False, "message": str(exc)},
        )

    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception) -> JSONResponse:
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": "Internal server error",
                "detail": str(exc),
            },
        )
