from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject
from pyrogram.client import Client
from pyrogram.types import CallbackQuery

from src.config import constants
from src.deps.main import MainContainer
from src.telegram.base.callback_query import CallbackQueryEndpoint
from src.telegram.templates import text as templates_text


class PaidCallbackQueryEndpoint(CallbackQueryEndpoint):
    callback_query_name: str = constants.PAID

    @inject
    async def handle(
        self,
        client: Client,
        callback_query: CallbackQuery,
        admin_id: str = Provide[MainContainer.config.telegram_admin_id],
    ) -> None:  # noqa: U100
        await client.answer_callback_query(callback_query.id)
        template = templates_text.PAID
        await callback_query.message.reply(
            text=template,
        )
        admin_template = templates_text.ADMIN.format(
            nick=callback_query.from_user.username,
            name=callback_query.from_user.first_name,
            last_name=callback_query.from_user.last_name,
        )
        await client.send_message(
            chat_id=admin_id,
            text=admin_template,
        )
