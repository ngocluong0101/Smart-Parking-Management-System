from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    project_name: str = "Smart Parking Management System"
    project_version: str = "0.1.0"
    debug: bool = True
    api_v1_prefix: str = "/api/v1"

    database_url: str = "mysql+mysqldb://root:password@localhost:3306/smart_parking"
    secret_key: str = "change-me"
    access_token_expire_minutes: int = 60


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
