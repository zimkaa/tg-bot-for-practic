from typing import List
from typing import Optional

from pyrogram import filters
from pyrogram.filters import Filter

from .message import MessageEndpoint


class PrivateCommandEndpoint(MessageEndpoint):
    commands: List[str] = []

    @classmethod
    def get_filters(cls) -> Optional[Filter]:
        return ~filters.forwarded & filters.private & filters.command(commands=cls.commands)
