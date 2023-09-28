from pyrogram.types import CallbackQuery


async def filter_callback(self, __, call: CallbackQuery) -> bool:
    return self.callback_query_name in call.data


async def filter_multi_callback(self, __, call: CallbackQuery) -> bool:
    return call.data in self.multi_callback_query_name
