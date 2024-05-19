from __future__ import annotations
from typing import TYPE_CHECKING

from pyrogram import filters

from .message import MessageEndpoint


if TYPE_CHECKING:
    from typing import ClassVar

    from pyrogram.filters import Filter


class PrivateCommandEndpoint(MessageEndpoint):
    commands: ClassVar[list[str]] = []

    @classmethod
    def get_filters(cls: type[PrivateCommandEndpoint]) -> Filter | None:
        return ~filters.forwarded & filters.private & filters.command(commands=cls.commands)
