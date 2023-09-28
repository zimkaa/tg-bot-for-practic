from typing import List

from pyrogram.client import Client
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

from src.config import constants
from src.telegram.base import PrivateCommandEndpoint
from src.telegram.base.callback_query import CallbackQueryEndpoint
from src.telegram.templates import text as templates_text


class FethiyeEndpoint(PrivateCommandEndpoint):
    commands: List[str] = [
        constants.FETHIYE,
    ]

    async def handle(
        self,
        client: Client,
        message: Message,
    ) -> None:  # noqa: U100
        template = templates_text.FETHIYE
        await client.send_message(
            chat_id=message.from_user.id,
            text=template,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text=constants.PAYMENT_TEXT, callback_data=f"{constants.PAYMENT}_{constants.FETHIYE}"
                        ),
                        InlineKeyboardButton(text=constants.MAIN_MENU, callback_data=constants.MENU),
                    ]
                ],
            ),
        )


class FethiyeCallbackQueryEndpoint(CallbackQueryEndpoint):
    callback_query_name: str = constants.FETHIYE

    async def handle(
        self,
        client: Client,
        callback_query: CallbackQuery,
    ) -> None:  # noqa: U100
        await client.answer_callback_query(callback_query.id)
        template = templates_text.FETHIYE
        await callback_query.message.reply(
            text=template,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text=constants.PAYMENT_TEXT, callback_data=f"{constants.PAYMENT}_{constants.FETHIYE}"
                        ),
                        InlineKeyboardButton(text=constants.MAIN_MENU, callback_data=constants.MENU),
                    ]
                ],
            ),
        )
