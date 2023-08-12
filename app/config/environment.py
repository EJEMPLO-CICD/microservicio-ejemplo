import os

from functools import lru_cache
from pydantic import BaseSettings
from cryptography.fernet import Fernet

class EnvironmentSettings(BaseSettings):
    DEBUG: bool = True
    APP_KEY: str = os.getenv("APP_KEY", str(Fernet.generate_key()))
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = os.getenv("REDIS_PORT", 6379)
    REDIS_USER: str = os.getenv("REDIS_USER", "homestead")
    REDIS_DB: str = os.getenv("REDIS_DB", 0)
    REDIS_PASSWORD: str = os.getenv("REDIS_PASSWORD", "secret")

@lru_cache
def get_environment_variables():
    return EnvironmentSettings()
