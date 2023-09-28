from pyrogram.client import Client
from pyrogram.types import CallbackQuery

from src.config import constants
from src.telegram.base.callback_query import CallbackQueryEndpoint
from src.telegram.templates import text as templates_text


class PaidCallbackQueryEndpoint(CallbackQueryEndpoint):
    callback_query_name: str = constants.PAID

    async def handle(
        self,
        client: Client,
        callback_query: CallbackQuery,
    ) -> None:  # noqa: U100
        await client.answer_callback_query(callback_query.id)
        template = templates_text.PAID
        await callback_query.message.reply(
            text=template,
        )
