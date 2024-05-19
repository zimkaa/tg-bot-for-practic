from __future__ import annotations
from typing import TYPE_CHECKING

from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup

from src.config import constants
from src.config import photo_ids
from src.deps.main import MainContainer
from src.telegram.base import CallbackQueryEndpoint
from src.telegram.base import PrivateCommandEndpoint
from src.telegram.templates import text as templates_text


if TYPE_CHECKING:
    from logging import Logger
    from typing import ClassVar

    from pyrogram.client import Client
    from pyrogram.types import CallbackQuery
    from pyrogram.types import Message


class StartEndpoint(PrivateCommandEndpoint):
    commands: ClassVar[list[str]] = [
        constants.START,
    ]

    @inject
    async def handle(
        self,
        client: Client,
        message: Message,
        admin_id: str = Provide[MainContainer.config.TELEGRAM_ADMIN_ID],
        logger: Logger = Provide[MainContainer.config.LOGGER],
    ) -> None:
        await client.send_message(
            chat_id=message.from_user.id,
            text=templates_text.START,
        )
        try:
            await client.send_photo(
                chat_id=message.from_user.id,
                photo=photo_ids.START,
            )
        except Exception as exc:
            logger.exception("Error: %s", exc)
            await client.send_message(
                chat_id=admin_id,
                text=templates_text.PHOTO_PROBLEM,
            )
        template = templates_text.MENU
        await client.send_message(
            chat_id=message.from_user.id,
            text=template,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=constants.GUIDE_SOUTH, callback_data=constants.SOUTH),
                        InlineKeyboardButton(text=constants.GUIDE_KAS, callback_data=constants.KAS),
                    ],
                ],
            ),
        )


class MenuEndpoint(PrivateCommandEndpoint):
    commands: ClassVar[list[str]] = [
        constants.MENU,
    ]

    @inject
    async def handle(
        self,
        client: Client,
        message: Message,
        admin_id: str = Provide[MainContainer.config.TELEGRAM_ADMIN_ID],
        logger: Logger = Provide[MainContainer.config.LOGGER],
    ) -> None:
        try:
            await client.send_photo(
                chat_id=message.from_user.id,
                photo=photo_ids.START,
            )
        except Exception as exc:
            logger.exception("Error: %s", exc)
            await client.send_message(
                chat_id=admin_id,
                text=templates_text.PHOTO_PROBLEM,
            )
        template = templates_text.MENU
        await client.send_message(
            chat_id=message.from_user.id,
            text=template,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=constants.GUIDE_SOUTH, callback_data=constants.SOUTH),
                        InlineKeyboardButton(text=constants.GUIDE_KAS, callback_data=constants.KAS),
                    ],
                ],
            ),
        )


class MenuCallbackQueryEndpoint(CallbackQueryEndpoint):
    callback_query_name: str = constants.MENU

    @inject
    async def handle(
        self,
        client: Client,
        callback_query: CallbackQuery,
        admin_id: str = Provide[MainContainer.config.TELEGRAM_ADMIN_ID],
        logger: Logger = Provide[MainContainer.config.LOGGER],
    ) -> None:
        await client.answer_callback_query(callback_query.id)
        try:
            await client.send_photo(
                chat_id=callback_query.from_user.id,
                photo=photo_ids.START,
            )
        except Exception as exc:
            logger.exception("Error: %s", exc)
            await client.send_message(
                chat_id=admin_id,
                text=templates_text.PHOTO_PROBLEM,
            )
        template = templates_text.MENU
        await callback_query.message.reply(
            text=template,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=constants.GUIDE_SOUTH, callback_data=constants.SOUTH),
                        InlineKeyboardButton(text=constants.GUIDE_KAS, callback_data=constants.KAS),
                    ],
                ],
            ),
        )
