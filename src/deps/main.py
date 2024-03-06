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
        name=config.TELEGRAM_BOT_NAME,
        bot_token=config.TELEGRAM_BOT_TOKEN,
        api_id=config.TELEGRAM_API_ID,
        api_hash=config.TELEGRAM_API_HASH,
        # TODO: Store in database
        in_memory=False,
    )
