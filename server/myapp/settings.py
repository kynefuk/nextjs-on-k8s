from typing import List
from pydantic import BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:3000",
        "http://34.107.239.159",
    ]


settings = Settings(PROJECT_NAME="hoge")
