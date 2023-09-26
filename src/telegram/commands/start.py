from typing import List

from pyrogram.client import Client
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

from src.config import constants
from src.telegram.base import CallbackQueryEndpoint, PrivateCommandEndpoint
from src.telegram.templates import text as templates_text


class StartEndpoint(PrivateCommandEndpoint):
    commands: List[str] = [
        constants.START,
        constants.MENU,
    ]

    async def handle(
        self,
        client: Client,
        message: Message,
    ) -> None:  # noqa: U100
        template = templates_text.MENU
        await client.send_message(
            chat_id=message.from_user.id,
            text=template,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=constants.GUIDE_FETHIYE, callback_data=constants.FETHIYE),
                        InlineKeyboardButton(text=constants.GUIDE_KAS, callback_data=constants.KAS),
                    ]
                ],
            ),
        )


class StartCallbackQueryEndpoint(CallbackQueryEndpoint):
    callback_query_name: str = constants.MENU

    async def handle(
        self,
        client: Client,
        callback_query: CallbackQuery,
    ) -> None:  # noqa: U100
        await client.answer_callback_query(callback_query.id)
        template = templates_text.PAYMENTS_INFO
        await callback_query.message.reply(
            text=template,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=constants.GUIDE_FETHIYE, callback_data=constants.FETHIYE),
                        InlineKeyboardButton(text=constants.GUIDE_KAS, callback_data=constants.KAS),
                    ]
                ],
            ),
        )
