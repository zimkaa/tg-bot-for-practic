from time import sleep

from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject
from pyrogram import idle
from pyrogram.client import Client as TelegramClient
from pyrogram.errors import FloodWait
from pyrogram.types import BotCommand

from bot.config import constants
from bot.deps.main import MainContainer
from bot.telegram.commands.kas import KasCallbackQueryEndpoint
from bot.telegram.commands.kas import KasEndpoint
from bot.telegram.commands.paid import PaidCallbackQueryEndpoint
from bot.telegram.commands.payment import PaymentCallbackQueryEndpoint
from bot.telegram.commands.payments_info import PaymentsInfoCallbackQueryEndpoint
from bot.telegram.commands.south import FethiyeCallbackQueryEndpoint
from bot.telegram.commands.south import FethiyeEndpoint

# from bot.telegram.commands.payments_info import PaymentsInfoCallbackQueryEndpoint
# from bot.telegram.commands.special_offer import OfferCallbackQueryEndpoint, OfferEndpoint
from bot.telegram.commands.start import MenuCallbackQueryEndpoint
from bot.telegram.commands.start import MenuEndpoint
from bot.telegram.commands.start import StartEndpoint


@inject
async def main(
    telegram: TelegramClient = Provide[MainContainer.telegram],
    app_version: str = Provide[MainContainer.config.app_version],
) -> None:
    """Run bot."""
    print(f"{app_version=}")
    telegram.add_handler(StartEndpoint().to_telegram_handler())

    telegram.add_handler(MenuEndpoint().to_telegram_handler())
    telegram.add_handler(KasEndpoint().to_telegram_handler())
    telegram.add_handler(FethiyeEndpoint().to_telegram_handler())
    # telegram.add_handler(PaymentsEndpoint().to_telegram_handler())
    # telegram.add_handler(OfferEndpoint().to_telegram_handler())

    telegram.add_handler(PaymentCallbackQueryEndpoint().to_telegram_handler())
    telegram.add_handler(PaymentsInfoCallbackQueryEndpoint().to_telegram_handler())
    telegram.add_handler(KasCallbackQueryEndpoint().to_telegram_handler())
    telegram.add_handler(FethiyeCallbackQueryEndpoint().to_telegram_handler())
    telegram.add_handler(PaidCallbackQueryEndpoint().to_telegram_handler())
    telegram.add_handler(MenuCallbackQueryEndpoint().to_telegram_handler())

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
            print(f"Wait {exc.value} seconds.")
            sleep(float(exc.value))
    finally:
        await telegram.stop()
