from typing import ClassVar

from pyrogram import filters
from pyrogram.filters import Filter

from .message import MessageEndpoint


class PrivateCommandEndpoint(MessageEndpoint):
    commands: ClassVar[list[str]] = []

    @classmethod
    def get_filters(cls: type["PrivateCommandEndpoint"]) -> Filter | None:
        return ~filters.forwarded & filters.private & filters.command(commands=cls.commands)
