from typing import List

from pyrogram.client import Client
from pyrogram.types import CallbackQuery, Message

from src.telegram.base import PrivateCommandEndpoint
from src.telegram.base.callback_query import CallbackQueryEndpoint
from src.telegram.templates.text import PAYMENTS_INFO


class PaymentsEndpoint(PrivateCommandEndpoint):
    commands: List[str] = [
        "payments_info",
    ]

    async def handle(
        self,
        client: Client,
        message: Message,
    ) -> None:  # noqa: U100
        template = PAYMENTS_INFO
        await self._send_message(
            chat_id=message.from_user.id,
            client=client,
            message=template,
        )


class PaymentsCallbackQueryEndpoint(CallbackQueryEndpoint):
    callback_query_name: str = "payments_info"

    async def handle(
        self,
        client: Client,
        callback_query: CallbackQuery,
    ) -> None:  # noqa: U100
        await client.answer_callback_query(callback_query.id)
        template = PAYMENTS_INFO
        await callback_query.message.reply(
            text=template,
        )
