import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Environment variables
    app_env: str = "development"
    log_level: str = "INFO"

    # We can add API keys here in the future
    # ai_api_key: str | None = None

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
