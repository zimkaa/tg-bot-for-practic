from typing import List

from pyrogram.client import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from src.telegram.base import PrivateCommandEndpoint
from src.telegram.templates import text as templates_text
from src.config import constants


class StartEndpoint(PrivateCommandEndpoint):
    commands: List[str] = [
        constants.START,
    ]

    async def handle(
        self,
        client: Client,
        message: Message,
    ) -> None:  # noqa: U100
        template = templates_text.START
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
