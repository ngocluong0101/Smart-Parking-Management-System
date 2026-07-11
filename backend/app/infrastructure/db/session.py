from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

def _create_engine(database_url: str):
	if database_url.startswith("sqlite"):
		return create_engine(database_url, connect_args={"check_same_thread": False}, future=True)

	try:
		return create_engine(database_url, pool_pre_ping=True, future=True)
	except ModuleNotFoundError:
		fallback_url = "sqlite:///./smart_parking.db"
		return create_engine(fallback_url, connect_args={"check_same_thread": False}, future=True)


engine = _create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()
