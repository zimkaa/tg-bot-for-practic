from pyrogram.client import Client
from pyrogram.types import CallbackQuery
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup

from src.config import constants
from src.telegram.base.callback_query import CallbackQueryEndpoint
from src.telegram.templates import text as templates_text


callback_strategy = {
    constants.RUS_PAYMENT: constants.RUS_PAID,
    constants.TRY_PAYMENT: constants.TRY_PAID,
    constants.OTHER_PAYMENT: constants.OTHER_PAID,
    constants.CRYPTO_PAYMENT: constants.CRYPTO_PAID,
}

templates_strategy = {
    constants.RUS_PAYMENT: templates_text.PAYMENTS_RUS_INFO,
    constants.TRY_PAYMENT: templates_text.PAYMENTS_TRY_INFO,
    constants.OTHER_PAYMENT: templates_text.PAYMENTS_OTHER_INFO,
    constants.CRYPTO_PAYMENT: templates_text.PAYMENTS_CRYPTO_INFO,
}


class PaymentCallbackQueryEndpoint(CallbackQueryEndpoint):
    callback_query_name: str = constants.PAYMENT_INFO

    async def handle(
        self,
        client: Client,
        callback_query: CallbackQuery,
    ) -> None:
        await client.answer_callback_query(callback_query.id)
        if not isinstance(callback_query.data, str):
            msg = "Callback query data is not str"
            raise Exception(msg)  # noqa: TRY004, TRY002
        query = callback_query.data.replace(f"_{constants.SOUTH}", "").replace(f"_{constants.KAS}", "")
        city = callback_query.data.split("_")[-1]
        template = templates_strategy[query]
        back_button = InlineKeyboardButton(text=constants.BACK_TEXT, callback_data=f"{constants.PAYMENT}_{city}")
        paid_button = InlineKeyboardButton(text=constants.PAID_TEXT, callback_data=constants.PAID)
        inline_reply_markup = [back_button]
        if query != constants.OTHER_PAYMENT:
            inline_reply_markup = [paid_button, *inline_reply_markup]
        await callback_query.message.reply(
            text=template,
            reply_markup=InlineKeyboardMarkup([inline_reply_markup]),
        )
