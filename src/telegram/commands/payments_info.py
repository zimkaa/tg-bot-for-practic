from pyrogram.client import Client
from pyrogram.types import CallbackQuery
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup

from src.config import constants
from src.telegram.base.callback_query import CallbackQueryEndpoint
from src.telegram.templates import text as templates_text


price_strategy = {
    constants.KAS: templates_text.PRICE_KAS,
    constants.SOUTH: templates_text.PRICE_SOUTH,
}


class PaymentsInfoCallbackQueryEndpoint(CallbackQueryEndpoint):
    callback_query_name: str = constants.PAYMENT

    async def handle(
        self,
        client: Client,
        callback_query: CallbackQuery,
    ) -> None:  # noqa: U100
        await client.answer_callback_query(callback_query.id)
        if not isinstance(callback_query.data, str):
            raise Exception("Callback query data is not str")
        place = callback_query.data.replace("payment_", "")
        price = price_strategy[place]
        template = templates_text.PAYMENTS_INFO.format(price=price)
        await callback_query.message.reply(
            text=template,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=constants.RUS_CARD, callback_data=f"{constants.RUS_PAYMENT}_{place}"),
                        InlineKeyboardButton(text=constants.TRY_CARD, callback_data=f"{constants.TRY_PAYMENT}_{place}"),
                    ],
                    [
                        InlineKeyboardButton(
                            text=constants.CRYPTO, callback_data=f"{constants.CRYPTO_PAYMENT}_{place}"
                        ),
                        InlineKeyboardButton(text=constants.OTHER, callback_data=f"{constants.OTHER_PAYMENT}_{place}"),
                    ],
                ],
            ),
        )
