from typing import List

from pyrogram.client import Client
from pyrogram.types import CallbackQuery
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import Message

from bot.config import constants
from bot.config import photo_ids
from bot.telegram.base import PrivateCommandEndpoint
from bot.telegram.base.callback_query import CallbackQueryEndpoint
from bot.telegram.templates import text as templates_text


class FethiyeEndpoint(PrivateCommandEndpoint):
    commands: List[str] = [
        constants.SOUTH,
    ]

    async def handle(
        self,
        client: Client,
        message: Message,
    ) -> None:  # noqa: U100
        await client.send_photo(
            chat_id=message.from_user.id,
            photo=photo_ids.SOUTH,
        )
        template = templates_text.SOUTH
        await client.send_message(
            chat_id=message.from_user.id,
            text=template,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text=constants.PAYMENT_TEXT, callback_data=f"{constants.PAYMENT}_{constants.SOUTH}"
                        ),
                        InlineKeyboardButton(text=constants.MAIN_MENU, callback_data=constants.MENU),
                    ]
                ],
            ),
        )


class FethiyeCallbackQueryEndpoint(CallbackQueryEndpoint):
    callback_query_name: str = constants.SOUTH

    async def handle(
        self,
        client: Client,
        callback_query: CallbackQuery,
    ) -> None:  # noqa: U100
        await client.answer_callback_query(callback_query.id)
        await client.send_photo(
            chat_id=callback_query.from_user.id,
            photo=photo_ids.SOUTH,
        )
        template = templates_text.SOUTH
        await callback_query.message.reply(
            text=template,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text=constants.PAYMENT_TEXT, callback_data=f"{constants.PAYMENT}_{constants.SOUTH}"
                        ),
                        InlineKeyboardButton(text=constants.MAIN_MENU, callback_data=constants.MENU),
                    ]
                ],
            ),
        )
