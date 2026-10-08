from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


PROJECT_ROOT = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):

    model_path: str
    threshold_path: str

    app_name: str
    app_version: str

    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        env_file_encoding="utf-8"
    )


settings = Settings()


MODEL_PATH = PROJECT_ROOT / settings.model_path
THRESHOLD_PATH = PROJECT_ROOT / settings.threshold_path