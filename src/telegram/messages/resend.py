from __future__ import annotations
from typing import TYPE_CHECKING

from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject

from src.deps.main import MainContainer
from src.telegram.base.message import MessageEndpoint


if TYPE_CHECKING:
    from pyrogram.client import Client
    from pyrogram.types import Message


class ResendFile(MessageEndpoint):
    @inject
    async def handle(
        self,
        client: Client,
        message: Message,
        admin_id: str = Provide[MainContainer.config.TELEGRAM_ADMIN_ID],
    ) -> None:
        await client.forward_messages(chat_id=admin_id, from_chat_id=message.chat.id, message_ids=message.id)
