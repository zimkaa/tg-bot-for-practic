from pyrogram.client import Client
from pyrogram.types import CallbackQuery
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup

from bot.config import constants
from bot.telegram.base.callback_query import CallbackQueryEndpoint
from bot.telegram.templates import text as templates_text


callback_strategy = {
    constants.RUS_PAYMENT: constants.RUS_PAID,
    constants.TRY_PAYMENT: constants.TRY_PAID,
    constants.U_MONEY_PAYMENT: constants.U_MONEY_PAID,
    constants.CRYPTO_PAYMENT: constants.CRYPTO_PAID,
}

templates_strategy = {
    constants.RUS_PAYMENT: templates_text.PAYMENTS_RUS_INFO,
    constants.TRY_PAYMENT: templates_text.PAYMENTS_TRY_INFO,
    constants.U_MONEY_PAYMENT: templates_text.PAYMENTS_U_MONEY_INFO,
    constants.CRYPTO_PAYMENT: templates_text.PAYMENTS_CRYPTO_INFO,
}


class PaymentCallbackQueryEndpoint(CallbackQueryEndpoint):
    callback_query_name: str = constants.PAYMENT_INFO

    async def handle(
        self,
        client: Client,
        callback_query: CallbackQuery,
    ) -> None:  # noqa: U100
        await client.answer_callback_query(callback_query.id)
        if not isinstance(callback_query.data, str):
            raise Exception("Callback query data is not str")
        query = callback_query.data.replace(f"_{constants.SOUTH}", "").replace(f"_{constants.KAS}", "")
        city = callback_query.data.split("_")[-1]
        template = templates_strategy[query]
        await callback_query.message.reply(
            text=template,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=constants.PAID_TEXT, callback_data=constants.PAID),
                        InlineKeyboardButton(text=constants.BACK, callback_data=f"{constants.PAYMENT}_{city}"),
                    ],
                ],
            ),
        )
