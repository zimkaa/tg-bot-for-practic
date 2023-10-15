import asyncio
from time import sleep
from typing import List
from typing import Optional

from pyrogram import filters
from pyrogram import idle
from pyrogram.client import Client
from pyrogram.errors import FloodWait
from pyrogram.filters import Filter
from pyrogram.handlers.message_handler import MessageHandler
from pyrogram.types import Message

from bot.config import constants
from bot.config import settings


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
    """Send to main account user_ID and respond for messages"""
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
        chat_id=settings.telegram_admin_id,
        text=text_to_admin,
    )


class EchoMessage:
    def to_telegram_handler(self) -> MessageHandler:
        return MessageHandler(callback=self.callback, filters=self.get_filters())  # type: ignore

    @classmethod
    def get_filters(cls) -> Optional[Filter]:
        return filters.text & filters.private

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
            print(exc)
            await message.reply(
                text="Error echo text",
                reply_to_message_id=message.id,
            )

    async def handle(
        self,
        client: Client,
        message: Message,
    ) -> None:  # noqa: U100
        await send_user_id(client=client, message=message)


class StartEchoEndpoint:
    commands: List[str] = [
        constants.START,
    ]

    def to_telegram_handler(self) -> MessageHandler:
        return MessageHandler(callback=self.callback, filters=self.get_filters())  # type: ignore

    @classmethod
    def get_filters(cls) -> Optional[Filter]:
        return ~filters.forwarded & filters.private & filters.command(commands=cls.commands)

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
            print(exc)
            await message.reply(
                text="Error echo command",
                reply_to_message_id=message.id,
            )

    async def handle(
        self,
        client: Client,
        message: Message,
    ) -> None:  # noqa: U100
        await send_user_id(client=client, message=message)


async def main() -> None:
    """Send to main account user_ID and respond for messages"""
    telegram = Client(
        name=settings.telegram_bot_name,
        bot_token=settings.telegram_bot_token,
        api_id=settings.telegram_api_id,
        api_hash=settings.telegram_api_hash,
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
            print(f"Wait {exc.value} seconds.")
            sleep(float(exc.value))
    finally:
        await telegram.stop()


if __name__ == "__main__":
    asyncio.run(main())
