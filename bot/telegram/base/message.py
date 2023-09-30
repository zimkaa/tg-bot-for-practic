from typing import Optional

from pyrogram import filters
from pyrogram.client import Client
from pyrogram.filters import Filter
from pyrogram.handlers.message_handler import MessageHandler
from pyrogram.types import Message

from .endpoint import BaseEndpoint


class MessageEndpoint(BaseEndpoint):
    def to_telegram_handler(self) -> MessageHandler:
        return MessageHandler(callback=self.callback, filters=self.get_filters())  # type: ignore

    async def callback(
        self,
        client: Client,
        message: Message,
    ) -> None:  # noqa: U100
        try:
            return await self.handle(
                client=client,
                message=message,
            )
        except Exception as exc:
            self.logger.exception(exc)
            await message.reply(
                # text=jinja.get_template("unknown_error.jinja").render(),
                text="Error",
                reply_to_message_id=message.id,
            )

    async def handle(
        self,
        client: Client,  # noqa: U100
        message: Message,  # noqa: U100
    ) -> None:
        raise NotImplementedError()


class PrivateMessage(MessageEndpoint):
    @classmethod
    def get_filters(cls) -> Optional[Filter]:
        return ~filters.forwarded & filters.private
