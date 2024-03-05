from pyrogram.client import Client
from pyrogram.filters import Filter
from pyrogram.filters import create
from pyrogram.handlers.callback_query_handler import CallbackQueryHandler
from pyrogram.types import CallbackQuery

from .custom_filters import filter_callback
from .endpoint import BaseEndpoint


class CallbackQueryEndpoint(BaseEndpoint):
    callback_query_name: str

    def to_telegram_handler(self) -> CallbackQueryHandler:
        return CallbackQueryHandler(callback=self.callback, filters=self.get_filters())

    @classmethod
    def get_filters(cls: type["CallbackQueryEndpoint"]) -> Filter | None:
        if not cls.callback_query_name:
            return None
        return create(filter_callback, callback_query_name=cls.callback_query_name)

    async def callback(
        self,
        client: Client,
        callback_query: CallbackQuery,
    ) -> None:
        try:
            return await self.handle(
                client=client,
                callback_query=callback_query,
            )
        except Exception as exc:
            self.logger.exception(exc)
            await callback_query.answer(
                text="Server error.",
                show_alert=True,
            )

    async def handle(
        self,
        client: Client,
        callback_query: CallbackQuery,
    ) -> None:
        raise NotImplementedError
