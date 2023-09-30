from pyrogram import enums
from pyrogram.filters import create
from pyrogram.types import Message


async def filter_contact(_, __, message: Message) -> bool:
    if message.media:
        if message.contact.user_id == message.from_user.id:
            return message.media == enums.MessageMediaType.CONTACT
    return False


contact_filter = create(filter_contact)
