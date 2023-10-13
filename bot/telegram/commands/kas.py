from typing import List

from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject
from pyrogram.client import Client
from pyrogram.types import CallbackQuery
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import Message

from bot.config import constants
from bot.config import photo_ids
from bot.deps.main import MainContainer
from bot.telegram.base import CallbackQueryEndpoint
from bot.telegram.base import PrivateCommandEndpoint
from bot.telegram.templates import text as templates_text


class KasEndpoint(PrivateCommandEndpoint):
    commands: List[str] = [
        constants.KAS,
    ]

    @inject
    async def handle(
        self,
        client: Client,
        message: Message,
        admin_id: str = Provide[MainContainer.config.telegram_admin_id],
    ) -> None:  # noqa: U100
        try:
            await client.send_photo(
                chat_id=message.from_user.id,
                photo=photo_ids.KAS,
            )
        except Exception:
            await client.send_message(
                chat_id=admin_id,
                text=templates_text.PHOTO_PROBLEM,
            )
        template = templates_text.KAS
        await client.send_message(
            chat_id=message.from_user.id,
            text=template,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text=constants.PAYMENT_TEXT, callback_data=f"{constants.PAYMENT}_{constants.KAS}"
                        ),
                        InlineKeyboardButton(text=constants.MAIN_MENU, callback_data=constants.MENU),
                    ]
                ],
            ),
        )


class KasCallbackQueryEndpoint(CallbackQueryEndpoint):
    callback_query_name: str = constants.KAS

    @inject
    async def handle(
        self,
        client: Client,
        callback_query: CallbackQuery,
        admin_id: str = Provide[MainContainer.config.telegram_admin_id],
    ) -> None:  # noqa: U100
        await client.answer_callback_query(callback_query.id)
        try:
            await client.send_photo(
                chat_id=callback_query.from_user.id,
                photo=photo_ids.KAS,
            )
        except Exception:
            await client.send_message(
                chat_id=admin_id,
                text=templates_text.PHOTO_PROBLEM,
            )
        template = templates_text.KAS
        await callback_query.message.reply(
            text=template,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text=constants.PAYMENT_TEXT, callback_data=f"{constants.PAYMENT}_{constants.KAS}"
                        ),
                        InlineKeyboardButton(text=constants.MAIN_MENU, callback_data=constants.MENU),
                    ]
                ],
            ),
        )
