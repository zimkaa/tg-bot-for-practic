from typing import List

from pyrogram.client import Client
from pyrogram.types import CallbackQuery
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import Message

from src.config import constants
from src.config import photo_ids
from src.telegram.base import CallbackQueryEndpoint
from src.telegram.base import PrivateCommandEndpoint
from src.telegram.templates import text as templates_text


class KasEndpoint(PrivateCommandEndpoint):
    commands: List[str] = [
        constants.KAS,
    ]

    async def handle(
        self,
        client: Client,
        message: Message,
    ) -> None:  # noqa: U100
        await client.send_photo(
            chat_id=message.from_user.id,
            photo=photo_ids.KAS,
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

    async def handle(
        self,
        client: Client,
        callback_query: CallbackQuery,
    ) -> None:  # noqa: U100
        await client.answer_callback_query(callback_query.id)
        template = templates_text.KAS
        await client.send_photo(
            chat_id=callback_query.from_user.id,
            photo=photo_ids.KAS,
        )
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
