from __future__ import annotations
from typing import TYPE_CHECKING

from pyrogram.handlers.message_handler import MessageHandler

from .endpoint import BaseEndpoint


if TYPE_CHECKING:
    from pyrogram.client import Client
    from pyrogram.types import Message


class MessageEndpoint(BaseEndpoint):
    def to_telegram_handler(self) -> MessageHandler:
        return MessageHandler(callback=self.callback, filters=self.get_filters())

    async def callback(
        self,
        client: Client,
        message: Message,
    ) -> None:
        try:
            return await self.handle(
                client=client,
                message=message,
            )
        except Exception as exc:
            self.logger.exception(exc)
            await message.reply(
                text="Error",
                reply_to_message_id=message.id,
            )

    async def handle(
        self,
        client: Client,
        message: Message,
    ) -> None:
        raise NotImplementedError
