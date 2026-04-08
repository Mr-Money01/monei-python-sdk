from enum import Enum


class DepositMethods(str, Enum):
    BANK_TRANSFER = "BANK_TRANSFER"
    USSD = "USSD"
    CARD = "CARD"


class NextActionType(str, Enum):
    requires_pin = "requires_pin"
    requires_otp = "requires_otp"
    redirect_url = "redirect_url"
    requires_additional_fields = "requires_additional_fields"
    payment_Instructions = "payment_Instructions"
 

class PaymentStatus(str, Enum):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"

class DepositAuthType(str, Enum):
    pin="pin"
    otp="otp"
    avs="avs"
    redirect_url="redirect_url" 
    payment_instruction="payment_instruction"

class AccountType(str, Enum):
    """Account type enumeration"""
    FIAT = "FIAT"
    CRYPTO = "CRYPTO"

    
 