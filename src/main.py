from logging import Logger
from time import sleep

from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject
from pyrogram import idle
from pyrogram.client import Client as TelegramClient
from pyrogram.errors import FloodWait
from pyrogram.types import BotCommand

from src.config import constants
from src.deps.main import MainContainer
from src.telegram.commands.kas import KasCallbackQueryEndpoint
from src.telegram.commands.kas import KasEndpoint
from src.telegram.commands.paid import PaidCallbackQueryEndpoint
from src.telegram.commands.payment import PaymentCallbackQueryEndpoint
from src.telegram.commands.payments_info import PaymentsInfoCallbackQueryEndpoint
from src.telegram.commands.south import FethiyeCallbackQueryEndpoint
from src.telegram.commands.south import FethiyeEndpoint
from src.telegram.commands.start import MenuCallbackQueryEndpoint
from src.telegram.commands.start import MenuEndpoint
from src.telegram.commands.start import StartEndpoint
from src.telegram.messages.resend import ResendFile


@inject
async def main(
    telegram: TelegramClient = Provide[MainContainer.telegram],
    app_version: str = Provide[MainContainer.config.APP_VERSION],
    logger: Logger = Provide[MainContainer.config.LOGGER],
) -> None:
    """Run bot."""
    logger.getChild(__name__)
    logger.info("Bot version: %s", app_version)
    telegram.add_handler(StartEndpoint().to_telegram_handler())

    telegram.add_handler(MenuEndpoint().to_telegram_handler())
    telegram.add_handler(KasEndpoint().to_telegram_handler())
    telegram.add_handler(FethiyeEndpoint().to_telegram_handler())

    telegram.add_handler(PaymentCallbackQueryEndpoint().to_telegram_handler())
    telegram.add_handler(PaymentsInfoCallbackQueryEndpoint().to_telegram_handler())
    telegram.add_handler(KasCallbackQueryEndpoint().to_telegram_handler())
    telegram.add_handler(FethiyeCallbackQueryEndpoint().to_telegram_handler())
    telegram.add_handler(PaidCallbackQueryEndpoint().to_telegram_handler())
    telegram.add_handler(MenuCallbackQueryEndpoint().to_telegram_handler())

    telegram.add_handler(ResendFile().to_telegram_handler())

    await telegram.start()
    commands = [
        BotCommand(constants.MENU, constants.MAIN_MENU),
        BotCommand(constants.KAS, constants.GUIDE_KAS),
        BotCommand(constants.SOUTH, constants.GUIDE_SOUTH),
    ]
    await telegram.set_bot_commands(commands=commands)
    await telegram.set_chat_menu_button()

    try:
        await idle()
    except FloodWait as exc:
        # TODO: Logging
        # TODO: BOT INFO
        if isinstance(exc.value, int):
            logger.info("Wait %s seconds.", exc.value)
            sleep(float(exc.value))  # noqa: ASYNC101
    finally:
        await telegram.stop()
