from dependency_injector import containers
from dependency_injector import providers
from pyrogram.client import Client as TelegramClient

from src.config import settings


class MainContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=[
            "bot",
            "bot.telegram.base.endpoint",
        ],
    )

    config = providers.Configuration(pydantic_settings=[settings])

    telegram = providers.Factory(
        TelegramClient,
        name=config.TELEGRAM_BOT_NAME,  # type: ignore[attr-defined]
        bot_token=config.TELEGRAM_BOT_TOKEN,  # type: ignore[attr-defined]
        api_id=config.TELEGRAM_API_ID,  # type: ignore[attr-defined]
        api_hash=config.TELEGRAM_API_HASH,  # type: ignore[attr-defined]
        # TODO: Store in database
        in_memory=False,
    )
