from __future__ import annotations
from abc import ABC
from typing import TYPE_CHECKING

from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject
from pyrogram.types import KeyboardButton
from pyrogram.types import Message
from pyrogram.types import ReplyKeyboardMarkup

from src.deps.main import MainContainer


if TYPE_CHECKING:
    from logging import Logger

    from pyrogram.client import Client
    from pyrogram.filters import Filter
    from pyrogram.handlers.handler import Handler


class BaseEndpoint(ABC):
    filters: Filter | None = None

    @inject
    def __init__(
        self,
        logger: Logger = Provide[MainContainer.config.LOGGER],
    ) -> None:
        super().__init__()
        self.logger = logger.getChild(self.__class__.__name__)

    def to_telegram_handler(self) -> Handler:
        raise NotImplementedError

    @classmethod
    def get_filters(cls: type[BaseEndpoint]) -> Filter | None:
        return cls.filters

    async def _request_contacts(
        self,
        chat_id: int,
        client: Client,
        message: str | None = None,
    ) -> Message:
        if not message:
            message = "To access all commands, you need to share a contact"
        return await client.send_message(
            chat_id=chat_id,
            text=message,
            reply_markup=ReplyKeyboardMarkup(
                [
                    [
                        KeyboardButton(text="Share your contacts", request_contact=True),
                    ],
                ],
                resize_keyboard=True,
            ),
        )

    async def _send_message(
        self,
        chat_id: int,
        client: Client,
        message: str | None = None,
    ) -> Message:
        if not message:
            message = "Some trouble"
        return await client.send_message(
            chat_id=chat_id,
            text=message,
        )
