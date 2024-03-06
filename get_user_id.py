from __future__ import annotations
import asyncio
from time import sleep
from typing import TYPE_CHECKING
from typing import ClassVar

from pyrogram import filters
from pyrogram import idle
from pyrogram.client import Client
from pyrogram.errors import FloodWait
from pyrogram.handlers.message_handler import MessageHandler

from src.config import constants
from src.config import settings


if TYPE_CHECKING:
    from pyrogram.filters import Filter
    from pyrogram.types import Message


TEXT = """
Написал пользователь:
username=`{username}`
first_name=`{first_name}`
last_name=`{last_name}`
id=`{id}`
"""


async def send_user_id(
    *,
    client: Client,
    message: Message,
) -> None:
    """Send to main account user_ID and respond for messages."""
    await client.send_message(
        chat_id=message.from_user.id,
        text=f"Your ID: {message.from_user.id}",
    )
    text_to_admin = TEXT.format(
        id=message.from_user.id,
        username=message.from_user.username if message.from_user.username else "None username",
        first_name=message.from_user.first_name if message.from_user.first_name else "None first_name",
        last_name=message.from_user.last_name if message.from_user.last_name else "None last_name",
    )
    await client.send_message(
        chat_id=settings.TELEGRAM_ADMIN_ID,
        text=text_to_admin,
    )


class EchoMessage:
    def to_telegram_handler(self) -> MessageHandler:
        return MessageHandler(callback=self.callback, filters=self.get_filters())  # type: ignore  # noqa: PGH003

    @classmethod
    def get_filters(cls: type[EchoMessage]) -> Filter | None:
        return filters.text & filters.private

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
        except Exception:  # noqa: BLE001
            await message.reply(
                text="Error echo text",
                reply_to_message_id=message.id,
            )

    async def handle(
        self,
        client: Client,
        message: Message,
    ) -> None:
        await send_user_id(client=client, message=message)


class StartEchoEndpoint:
    commands: ClassVar[list[str]] = [
        constants.START,
    ]

    def to_telegram_handler(self) -> MessageHandler:
        return MessageHandler(callback=self.callback, filters=self.get_filters())  # type: ignore  # noqa: PGH003

    @classmethod
    def get_filters(cls: type[StartEchoEndpoint]) -> Filter | None:
        return ~filters.forwarded & filters.private & filters.command(commands=cls.commands)

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
        except Exception:  # noqa: BLE001
            await message.reply(
                text="Error echo command",
                reply_to_message_id=message.id,
            )

    async def handle(
        self,
        client: Client,
        message: Message,
    ) -> None:
        await send_user_id(client=client, message=message)


async def main() -> None:
    """Send to main account user_ID and respond for messages."""
    telegram = Client(
        name=settings.TELEGRAM_BOT_NAME,
        bot_token=settings.TELEGRAM_BOT_TOKEN,
        api_id=settings.TELEGRAM_API_ID,
        api_hash=settings.TELEGRAM_API_HASH,
    )
    telegram.add_handler(EchoMessage().to_telegram_handler())
    telegram.add_handler(StartEchoEndpoint().to_telegram_handler())

    await telegram.start()

    try:
        await idle()
    except FloodWait as exc:
        # TODO: Logging
        # TODO: BOT INFO
        if isinstance(exc.value, int):
            sleep(float(exc.value))  # noqa: ASYNC101
    finally:
        await telegram.stop()


if __name__ == "__main__":
    asyncio.run(main())
