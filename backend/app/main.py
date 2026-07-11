from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import configure_logging
from app.infrastructure.db.init_db import init_db


def create_app() -> FastAPI:
    configure_logging()

    app = FastAPI(
        title=settings.project_name,
        version=settings.project_version,
        debug=settings.debug,
    )

    register_exception_handlers(app)
    app.include_router(api_router, prefix=settings.api_v1_prefix)

    @app.on_event("startup")
    def startup_event() -> None:
        init_db()

    return app


app = create_app()
