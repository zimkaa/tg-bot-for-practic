from pyrogram.types import CallbackQuery


async def filter_callback(self, __, call: CallbackQuery) -> bool:
    return self.callback_query_name in call.data
