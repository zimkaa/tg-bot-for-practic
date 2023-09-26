import logging

import pydantic
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


pydantic.BaseSettings = BaseSettings


class Settings(BaseSettings):
    app_version: str = "0.1"

    # Project settings:
    project_name: str = "SalesBody"

    # development / test / production
    environment: str = "development"
    debug: bool = False
    logger: logging.Logger = logging.getLogger("SalesLogger")

    telegram_bot_name: str
    telegram_bot_token: str
    telegram_api_id: int
    telegram_api_hash: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
