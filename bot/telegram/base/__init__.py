from .callback_query import CallbackQueryEndpoint
from .command import PrivateCommandEndpoint
from .contact_message import ContactMessageEndpoint
from .message import PrivateMessage


__all__ = [
    "PrivateCommandEndpoint",
    "CallbackQueryEndpoint",
    "ContactMessageEndpoint",
    "PrivateMessage",
]
