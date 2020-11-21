from typing import List
from pydantic import BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []


settings = Settings(PROJECT_NAME="hoge")
