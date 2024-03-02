from pyrogram.client import Client
from pyrogram.handlers.message_handler import MessageHandler
from pyrogram.types import Message

from .endpoint import BaseEndpoint


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
            self.logger.exception(exc)  # noqa: TRY401
            await message.reply(
                # text=jinja.get_template("unknown_error.jinja").render(),
                text="Error",
                reply_to_message_id=message.id,
            )

    async def handle(
        self,
        client: Client,
        message: Message,
    ) -> None:
        raise NotImplementedError
