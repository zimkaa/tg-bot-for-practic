import logging

import pydantic
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


pydantic.BaseSettings = BaseSettings


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_version: str = "0.1.0"

    # Project settings:
    project_name: str = "SalesBot"

    # development / test / production
    environment: str = "development"
    debug: bool = False
    logger: logging.Logger = logging.getLogger("SalesLogger")

    # Telegram settings:
    telegram_admin_id: int = 5218682536
    telegram_bot_name: str = "default_bot"
    telegram_bot_token: str = "default_token"
    # telegram_api_id: int
    # telegram_api_hash: str


settings = Settings()
