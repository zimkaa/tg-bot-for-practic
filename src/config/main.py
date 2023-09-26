import logging

import pydantic
from pydantic_settings import BaseSettings, SettingsConfigDict


pydantic.BaseSettings = BaseSettings


class Settings(BaseSettings):
    app_version: str = "0.1"

    # Project settings:
    project_name: str = "SalesBody"

    # development / test / production
    environment: str = "development"
    debug: bool = False
    logger: logging.Logger = logging.getLogger("SalesLogger")

    telegram_bot_name: str = "bot"
    telegram_bot_token: str = "7549872880:BBFfxlbArNhajdYHtoD5rOhBV-gs2Eurk8g"  # cspell:disable-line
    telegram_api_id: int = 1328051
    telegram_api_hash: str = "dde5bd5420266051f4755g6b5da8281b"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
