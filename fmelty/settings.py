from meltano.core.project import Project
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    host: str = "127.0.0.1"
    port: int = 8000

    app_name: str = "fmelty - fastapi expirementation"
    project: Project = Project.find()

    meltano_environment: str = "dev"

    class Config:
        env_file = ".env"
        env_prefix = "FMELTY_"
        env_file_encoding = "utf-8"


settings = Settings()
