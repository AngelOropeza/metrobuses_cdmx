import os
from loguru import logger

from pydantic import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """General settings."""

    try:
        # DB
        db_host: Optional[str] = os.getenv("DB_HOST", "0.0.0.0")
        db_password: Optional[str] = os.getenv("DB_PASS", "secret")
        db_name: Optional[str] = os.getenv("DB_NAME", "metrobuses")
        db_user: Optional[str] = os.getenv("DB_USER", "postgres")
        db_port: Optional[str] = os.getenv("DB_PORT", "5432")

    except KeyError as e:
        logger.error(f"Please set the environment variable {e}")
        raise


def get_settings():
    """Get general settings."""
    return Settings()


settings = get_settings()