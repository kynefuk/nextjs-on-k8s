from typing import List
from pydantic import BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:3000",
        "http://34.107.239.159",
        "https://d6o1z4uikxewi.cloudfront.net",
    ]


settings = Settings(PROJECT_NAME="hoge")
