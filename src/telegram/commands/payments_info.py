from pyrogram.client import Client
from pyrogram.types import CallbackQuery
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup

from src.config import constants
from src.telegram.base.callback_query import CallbackQueryEndpoint
from src.telegram.templates import text as templates_text


class PaymentsInfoCallbackQueryEndpoint(CallbackQueryEndpoint):
    callback_query_name: str = constants.PAYMENT

    async def handle(
        self,
        client: Client,
        callback_query: CallbackQuery,
    ) -> None:  # noqa: U100
        await client.answer_callback_query(callback_query.id)
        city = callback_query.data.replace("payment_", "")
        template = templates_text.PAYMENTS_INFO
        await callback_query.message.reply(
            text=template,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=constants.RUS_CARD, callback_data=f"{constants.RUS_PAYMENT}_{city}"),
                        InlineKeyboardButton(text=constants.TRY_CARD, callback_data=f"{constants.TRY_PAYMENT}_{city}"),
                    ],
                    [
                        InlineKeyboardButton(
                            text=constants.U_MONEY, callback_data=f"{constants.U_MONEY_PAYMENT}_{city}"
                        ),
                        InlineKeyboardButton(text=constants.CRYPTO, callback_data=f"{constants.CRYPTO_PAYMENT}_{city}"),
                    ],
                ],
            ),
        )
