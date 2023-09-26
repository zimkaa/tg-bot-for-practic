from time import sleep

from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject
from pyrogram import idle
from pyrogram.client import Client as TelegramClient
from pyrogram.errors import FloodWait
from pyrogram.types import BotCommand

from src.config import constants
from src.deps.main import MainContainer
from src.telegram.commands.fethiye import FethiyeCallbackQueryEndpoint
from src.telegram.commands.fethiye import FethiyeEndpoint
from src.telegram.commands.kas import KasCallbackQueryEndpoint
from src.telegram.commands.kas import KasEndpoint
from src.telegram.commands.payments_info import PaymentsCallbackQueryEndpoint
from src.telegram.commands.payments_info import PaymentsEndpoint
from src.telegram.commands.special_offer import OfferCallbackQueryEndpoint
from src.telegram.commands.special_offer import OfferEndpoint
from src.telegram.commands.start import StartEndpoint


@inject
async def main(telegram: TelegramClient = Provide[MainContainer.telegram]) -> None:
    """Run bot."""
    telegram.add_handler(StartEndpoint().to_telegram_handler())
    telegram.add_handler(KasEndpoint().to_telegram_handler())
    telegram.add_handler(FethiyeEndpoint().to_telegram_handler())
    # telegram.add_handler(PaymentsEndpoint().to_telegram_handler())
    # telegram.add_handler(OfferEndpoint().to_telegram_handler())

    telegram.add_handler(KasCallbackQueryEndpoint().to_telegram_handler())
    telegram.add_handler(FethiyeCallbackQueryEndpoint().to_telegram_handler())
    # telegram.add_handler(PaymentsCallbackQueryEndpoint().to_telegram_handler())
    # telegram.add_handler(OfferCallbackQueryEndpoint().to_telegram_handler())

    await telegram.start()
    commands = [
        BotCommand(constants.START, constants.MAIN_MENU),
        BotCommand(constants.KAS, constants.GUIDE_KAS),
        BotCommand(constants.FETHIYE, constants.GUIDE_FETHIYE),
        # BotCommand("payments_info", "Условия оплаты"),
        # BotCommand("delivery_info", "Условия доставки"),
    ]
    await telegram.set_bot_commands(commands=commands)
    await telegram.set_chat_menu_button()

    try:
        await idle()
    except FloodWait as exc:
        # TODO: Logging
        # TODO: BOT INFO
        if isinstance(exc.value, int):
            print(f"Wait {exc.value} seconds.")
            sleep(float(exc.value))
    finally:
        await telegram.stop()
