import asyncio
from time import sleep
from typing import Optional

from pyrogram import enums
from pyrogram import filters
from pyrogram import idle
from pyrogram.client import Client
from pyrogram.errors import FloodWait
from pyrogram.filters import Filter
from pyrogram.filters import create
from pyrogram.handlers.message_handler import MessageHandler
from pyrogram.types import Message

from src.config import settings


TEXT = """
Пользователь отправил фото:
username=`{username}`
first_name=`{first_name}`
last_name=`{last_name}`
id=`{id}`
file_type=`{file_type}`
file_id=`{file_id}`
"""


async def filter_file_or_photo(_, __, message: Message) -> bool:
    if message.media:
        return message.media in (enums.MessageMediaType.DOCUMENT, enums.MessageMediaType.PHOTO)
    return False


file_or_photo_filter = create(filter_file_or_photo)


async def send_user_id(
    *,
    client: Client,
    message: Message,
) -> None:
    """Send to main account user_ID and respond for messages."""
    if message.media == enums.MessageMediaType.DOCUMENT:
        file_id = message.document.file_id if message.document else "In message no document"
    else:
        file_id = message.photo.file_id if message.photo else "In message no photo"
    await client.send_message(
        chat_id=message.from_user.id,
        text=f"file_type {message.media.value} file ID: `{file_id}`",
    )
    text_to_admin = TEXT.format(
        id=message.from_user.id,
        username=message.from_user.username if message.from_user.username else "None username",
        first_name=message.from_user.first_name if message.from_user.first_name else "None first_name",
        last_name=message.from_user.last_name if message.from_user.last_name else "None last_name",
        file_type=message.media.value,
        file_id=file_id,
    )
    await client.send_message(
        chat_id=settings.TELEGRAM_ADMIN_ID,
        text=text_to_admin,
    )


class EchoFileIDMessage:
    def to_telegram_handler(self) -> MessageHandler:
        return MessageHandler(callback=self.callback, filters=self.get_filters())  # type: ignore  # noqa: PGH003

    @classmethod
    def get_filters(cls) -> Optional[Filter]:
        return file_or_photo_filter & filters.private

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


async def main() -> None:
    """Send to main account user_ID and respond for messages."""
    telegram = Client(
        name=settings.TELEGRAM_BOT_NAME,
        bot_token=settings.TELEGRAM_BOT_TOKEN,
        api_id=settings.TELEGRAM_API_ID,
        api_hash=settings.TELEGRAM_API_HASH,
    )
    telegram.add_handler(EchoFileIDMessage().to_telegram_handler())

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
