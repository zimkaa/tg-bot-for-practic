from typing import List

from pyrogram.client import Client
from pyrogram.types import CallbackQuery, Message

from src.telegram.base import PrivateCommandEndpoint
from src.telegram.base.callback_query import CallbackQueryEndpoint
from src.telegram.templates.text import SPECIAL_OFFER


class OfferEndpoint(PrivateCommandEndpoint):
    commands: List[str] = [
        "special_offer",
    ]

    async def handle(
        self,
        client: Client,
        message: Message,
    ) -> None:  # noqa: U100
        template = SPECIAL_OFFER
        await self._send_message(
            chat_id=message.from_user.id,
            client=client,
            message=template,
        )


class OfferCallbackQueryEndpoint(CallbackQueryEndpoint):
    callback_query_name: str = "special_offer"

    async def handle(
        self,
        client: Client,
        callback_query: CallbackQuery,
    ) -> None:  # noqa: U100
        await client.answer_callback_query(callback_query.id)
        template = SPECIAL_OFFER
        await callback_query.message.reply(
            text=template,
        )
