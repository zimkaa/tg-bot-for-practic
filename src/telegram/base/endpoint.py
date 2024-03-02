from abc import ABC
from logging import Logger
from typing import Optional

from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject
from pyrogram.client import Client
from pyrogram.filters import Filter
from pyrogram.handlers.handler import Handler
from pyrogram.types import KeyboardButton
from pyrogram.types import Message
from pyrogram.types import ReplyKeyboardMarkup

from src.deps.main import MainContainer


class BaseEndpoint(ABC):
    filters: Optional[Filter] = None

    @inject
    def __init__(
        self,
        logger: Logger = Provide[MainContainer.config.logger],  # type: ignore
    ) -> None:
        super().__init__()
        self.logger = logger.getChild(self.__class__.__name__)

    def to_telegram_handler(self) -> Handler:
        raise NotImplementedError()

    @classmethod
    def get_filters(cls) -> Filter | None:
        return cls.filters

    async def _request_contacts(
        self,
        chat_id: int,
        client: Client,
        message: Optional[str] = None,
    ) -> Message:
        if not message:
            message = "To access all commands, you need to share a contact"
        send_message = await client.send_message(
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
        return send_message

    async def _send_message(
        self,
        chat_id: int,
        client: Client,
        message: Optional[str] = None,
    ) -> Message:
        if not message:
            message = "Some trouble"
        send_message = await client.send_message(
            chat_id=chat_id,
            text=message,
        )
        return send_message
