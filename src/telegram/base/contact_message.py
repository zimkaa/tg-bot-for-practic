from typing import Optional

from pyrogram.filters import Filter, forwarded, private

from src.telegram.custom_filter import contact_filter

from .message import MessageEndpoint


class ContactMessageEndpoint(MessageEndpoint):
    @classmethod
    def get_filters(cls) -> Optional[Filter]:
        return ~forwarded & private & contact_filter
