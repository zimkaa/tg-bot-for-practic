from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject
from pyrogram.client import Client
from pyrogram.types import CallbackQuery
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import Message

from src.config import constants
from src.config import photo_ids
from src.deps.main import MainContainer
from src.telegram.base import PrivateCommandEndpoint
from src.telegram.base.callback_query import CallbackQueryEndpoint
from src.telegram.templates import text as templates_text


class FethiyeEndpoint(PrivateCommandEndpoint):
    commands: list[str] = [
        constants.SOUTH,
    ]

    @inject
    async def handle(
        self,
        client: Client,
        message: Message,
        admin_id: str = Provide[MainContainer.config.TELEGRAM_ADMIN_ID],
    ) -> None:
        try:
            await client.send_photo(
                chat_id=message.from_user.id,
                photo=photo_ids.SOUTH,
            )
        except Exception:  # noqa: BLE001
            await client.send_message(
                chat_id=admin_id,
                text=templates_text.PHOTO_PROBLEM,
            )
        template = templates_text.SOUTH
        await client.send_message(
            chat_id=message.from_user.id,
            text=template,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text=constants.PAYMENT_TEXT,
                            callback_data=f"{constants.PAYMENT}_{constants.SOUTH}",
                        ),
                        InlineKeyboardButton(text=constants.MAIN_MENU, callback_data=constants.MENU),
                    ],
                ],
            ),
        )


class FethiyeCallbackQueryEndpoint(CallbackQueryEndpoint):
    callback_query_name: str = constants.SOUTH

    @inject
    async def handle(
        self,
        client: Client,
        callback_query: CallbackQuery,
        admin_id: str = Provide[MainContainer.config.TELEGRAM_ADMIN_ID],
    ) -> None:
        await client.answer_callback_query(callback_query.id)
        try:
            await client.send_photo(
                chat_id=callback_query.from_user.id,
                photo=photo_ids.SOUTH,
            )
        except Exception:  # noqa: BLE001
            await client.send_message(
                chat_id=admin_id,
                text=templates_text.PHOTO_PROBLEM,
            )
        template = templates_text.SOUTH
        await callback_query.message.reply(
            text=template,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text=constants.PAYMENT_TEXT,
                            callback_data=f"{constants.PAYMENT}_{constants.SOUTH}",
                        ),
                        InlineKeyboardButton(text=constants.MAIN_MENU, callback_data=constants.MENU),
                    ],
                ],
            ),
        )
