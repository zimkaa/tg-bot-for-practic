from pyrogram.client import Client
from pyrogram.types import CallbackQuery


async def filter_callback(self, client: Client, call: CallbackQuery) -> bool:
    return self.callback_query_name in call.data
