from dependency_injector import containers
from dependency_injector import providers
from pyrogram.client import Client as TelegramClient

from src.config import settings


class MainContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=[
            "src",
            "src.telegram.base.endpoint",
        ],
    )

    config = providers.Configuration(pydantic_settings=[settings])

    telegram = providers.Factory(
        TelegramClient,
        name=config.telegram_bot_name,  # type: ignore[attr-defined]
        bot_token=config.telegram_bot_token,  # type: ignore[attr-defined]
        # api_id=config.telegram_api_id,  # type: ignore[attr-defined]
        # api_hash=config.telegram_api_hash,  # type: ignore[attr-defined]
        # TODO: Store in database
        in_memory=False,
    )
