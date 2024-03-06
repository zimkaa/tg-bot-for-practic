from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyrogram.client import Client
    from pyrogram.types import CallbackQuery


async def filter_callback(self, client: Client, call: CallbackQuery) -> bool:
    return self.callback_query_name in call.data
