from typing import List

from pyrogram.client import Client
from pyrogram.types import CallbackQuery
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import Message

from src.config import constants
from src.telegram.base import PrivateCommandEndpoint
from src.telegram.base.callback_query import CallbackQueryEndpoint
from src.telegram.templates import text as templates_text


class PaymentsEndpoint(PrivateCommandEndpoint):
    commands: List[str] = [
        constants.PAYMENT,
    ]

    async def handle(
        self,
        client: Client,
        message: Message,
    ) -> None:  # noqa: U100
        template = templates_text.PAYMENTS_INFO
        await client.send_message(
            chat_id=message.from_user.id,
            client=client,
            message=template,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=constants.RUS_CARD, callback_data=constants.RUS_PAYMENT),
                        InlineKeyboardButton(text=constants.TRY_CARD, callback_data=constants.TRY_PAYMENT),
                    ],
                    [
                        InlineKeyboardButton(text=constants.U_MONEY, callback_data=constants.U_MONEY_PAYMENT),
                        InlineKeyboardButton(text=constants.CRYPTO, callback_data=constants.CRYPTO_PAYMENT),
                    ],
                ],
            ),
        )


class PaymentsCallbackQueryEndpoint(CallbackQueryEndpoint):
    callback_query_name: str = constants.PAYMENT

    async def handle(
        self,
        client: Client,
        callback_query: CallbackQuery,
    ) -> None:  # noqa: U100
        await client.answer_callback_query(callback_query.id)
        template = templates_text.PAYMENTS_INFO
        await callback_query.message.reply(
            text=template,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=constants.RUS_CARD, callback_data=constants.RUS_PAYMENT),
                        InlineKeyboardButton(text=constants.TRY_CARD, callback_data=constants.TRY_PAYMENT),
                    ],
                    [
                        InlineKeyboardButton(text=constants.U_MONEY, callback_data=constants.U_MONEY_PAYMENT),
                        InlineKeyboardButton(text=constants.CRYPTO, callback_data=constants.CRYPTO_PAYMENT),
                    ],
                ],
            ),
        )
