
from enum import Enum


class PaymentMethodType(str, Enum):
    BANK_TRANSFER = "BANK_TRANSFER"
    CARD = "CARD"
    USSD = "USSD"