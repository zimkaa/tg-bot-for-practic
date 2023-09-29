from pyrogram.client import Client
from pyrogram.filters import Filter
from pyrogram.filters import create
from pyrogram.handlers.callback_query_handler import CallbackQueryHandler
from pyrogram.types import CallbackQuery

from .custom_filters import filter_callback
from .custom_filters import filter_multi_callback
from .endpoint import BaseEndpoint


class CallbackQueryEndpoint(BaseEndpoint):
    callback_query_name: str | None = None

    def to_telegram_handler(self) -> CallbackQueryHandler:
        return CallbackQueryHandler(callback=self.callback, filters=self.get_filters())  # type: ignore

    @classmethod
    def get_filters(cls) -> Filter | None:
        if not cls.callback_query_name:
            return None
        callback_filter = create(filter_callback, callback_query_name=cls.callback_query_name)
        return callback_filter

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
        client: Client,  # noqa: U100
        callback_query: CallbackQuery,  # noqa: U100
    ) -> None:
        raise NotImplementedError()


class MultiCallbackQueryEndpoint(CallbackQueryEndpoint):
    multi_callback_query_name: list[str] | None = None

    @classmethod
    def get_filters(cls) -> Filter | None:
        if not cls.callback_query_name:
            return None
        callback_filter = create(filter_multi_callback, callback_query_name=cls.multi_callback_query_name)
        return callback_filter
