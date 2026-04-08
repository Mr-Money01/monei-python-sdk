"""Wallet-related models"""

from typing import Optional, Literal, Dict, Any,List
from pydantic import BaseModel
from datetime import datetime
from .base import BaseDto
from enum import Enum
from .enums.wallet import PaymentStatus, NextActionType, DepositAuthType, AccountType
    

class SubWalletDto(BaseDto):
    """Sub-wallet model"""
    parentWalletId: Optional[str] = None  # Make optional
    type: AccountType  # "FIAT" or "CRYPTO"
    currency: str
    balance: float
    chain: Optional[str] = None
    publicAddress: Optional[str] = None
    evmPortfolio: Optional[Dict[str, Any]] = None
    solPortfolio: Optional[Dict[str, Any]] = None

class SubWalletResponseDto(BaseModel):
    
    statusCode: int
    message: str 
    data: SubWalletDto
    errors:Optional[Dict[str, Any]] = None

class UserWalletDto(BaseModel):
    """User wallet model"""
    nairaBalance: str
    evmPortfolio: Optional[Dict[str, Any]] = None
    solPortfolio: Optional[Dict[str, Any]] = None
    subwallets: List[SubWalletDto]

class UserWalletResponseDto(BaseModel):
    
    statusCode: int
    message: str 
    data: UserWalletDto
    errors:Optional[Dict[str, Any]] = None

class GetNairaWalletResponseDto(BaseModel):
    """naira wallet details response model"""
    statusCode: int
    message: str 
    data: NairaWalletDto
    errors:Optional[Dict[str, Any]] = None

class NairaWalletDto(BaseModel):
    """naira wallet data model"""
    id: str
    type: AccountType
    virtualAccount: Optional[VirtualAccountDto] = None
    currency: str
    balance: float
    chain: Optional[str] = None
    publicAddress: Optional[str] = None
    createdAt: datetime
    updatedAt: datetime
    deletedDate: Optional[datetime] = None
    

class FundWalletByNairaDto(BaseModel):
    """Fund wallet request"""
    amount: float

class DepositResponseDto(BaseModel):
    """Deposit response"""
    link: str

class FundwalletResponseDto(BaseModel):
    """Fund wallet response"""
    statusCode: int
    message: str
    data: DepositResponseDto

class WithdrawWalletDto(BaseModel):
    """Withdraw to bank request"""
    amount: float
    bank: str
    accountNumber: str
    transactionPin: str
    currency: Optional[str] = "NGN"
    reference: Optional[str] = None
    narration: Optional[str] = None

class PeerTransferDto(BaseModel):
    """Peer transfer request"""
    receiver: str
    amount: float
    transactionPin: str
    currency: Optional[str] = "NGN"

class BankDto(BaseModel):
    """Bank model"""
    
    id: int
    code: str
    name: str
    

class BankAccountDto(BaseModel):
    """Bank account model"""
    accountName: str
    accountNumber: str
    bankCode: str
    bankName: str

class VerifyBankAccountRequestDto(BaseModel):
    """Bank account verification request"""
    accountNumber: str
    bank: str

class BankListResponseDto(BaseModel):
    """get bank response model"""
    statusCode: int
    message: str 
    data: List[BankDto]
    errors: Optional[dict] = None

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)



class VirtualAccountDto(BaseModel):
    id:str
    createdAt:str
    updatedAt:str
    deletedDate:str
    accountNumber:str
    bankName:str
    reference:str
    status:str
    isActive:bool
    deletedDate: Optional[datetime] = None

class VirtualAccountResponseDto(BaseModel):
    """virtual account response model"""
    statusCode: int
    message: str 
    data: Optional[VirtualAccountDto] = None
    errors: Optional[Any] = None

class CreateVirtualAccountDto(BaseModel):
    """virtual account request model"""
    nin: str
    reference: Optional[str] = None 

class AddCardDto(BaseModel):
    
    expiryMonth: str
    expiryYear: str 
    cardNumber: str
    cvv: str
    cardHolderName:str

class AddUsdtDto(BaseModel):
    
    bankCode: str
    
class DepositDto(BaseModel):
    amount:int
    reference:str
    currency:str
    card: Optional[AddCardDto]=None
    ussd: Optional[AddUsdtDto]=None
    narration:str

class DepositResponseDto(BaseModel):
    """Deposit response model"""
    statusCode: int
    message: str 
    data: Any
    errors: dict

class DepositNextActionDto(BaseModel):
    
    type: NextActionType
    redirect_url: dict
    payment_instruction: dict

class Customization(BaseModel):
    
    title: str
    
class Customer(BaseModel):
    
    email: str
    phoneNumber: str
    name: str

class PaymentDto(BaseModel):

    amount:int
    totalAmount:int
    reference:str
    currency:str
    redirectUrl: Optional[str] = None
    customization: Optional[Customization] = None
    customer: Optional[Customer] = None
    narration:str
    accountNumber:Optional[str] = None
    bankName:Optional[str] = None
    accountName:Optional[str] = None
    expiry_datetime:Optional[str] = None
    note:Optional[str] = None
    status:str
    nextAction:DepositNextActionDto

class InitiateBankTransferDto(BaseModel):
    """Deposit request model"""

    amount: int
    bank: str
    accountNumber: str
    transactionPin: str
    reference: str
    narration: Optional[str]=None
    meta:Optional[Dict[str, Any]] = None

class WithdrawWalletDto(BaseModel):
    
    amount: int
    bank: str
    accountNumber: str
    transactionPin: str
    currency: Optional[str]=None
    reference: Optional[str]=None
    narration: Optional[str]=None
   
class InitiateBankTransferResponseDto(BaseModel):
    
    statusCode: int
    message: str 
    data: InitiateBankTransferResponseDataDto
    errors: dict

class InitiateBankTransferResponseDataDto(BaseModel):
    
    reference: int
    status: PaymentStatus
    amount: int

class DepositWithPaymentMethodDto(BaseModel):
    """create payment request model"""

    amount: int
    paymentMethodId: str
    reference: str
    currency: str
    redirectUrl: str
    meta: Dict
    narration: str

class DepositWithPaymentMethodResponseDto(BaseModel):
    
    """deposit with payment response model"""
    statusCode: int
    message: str 
    data: DepositWithPaymentMethodResponseDataDto
    errors: Optional[dict] = None

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)
    
class DepositWithPaymentMethodResponseDataDto(BaseModel):

    reference: str
    amount: str
    status: str
    currency: str
    narration: str
    nextAction:PaymentMethodNextActionDto

class PaymentMethodNextActionDto(BaseModel):
    
    type: NextActionType
    requires_pin: Optional[dict] = None
    

class PaymentResponseDto(BaseModel):
    """payment response model"""
    statusCode: int
    message: str 
    data: PaymentDto
    errors: Optional[dict] = None

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)


class DepositAuthResponseDto(BaseModel):
    """authorize charge response model"""
    statusCode: int
    message: str 
    data: dict
    errors: dict

class DepositAuthDto(BaseModel):
    """authorize charge response model"""
    type: DepositAuthType
    reference: str 
    pin: Optional[str] = None
    otp: Optional[str] = None
    avs: FlwAvsAuthDto

class FlwAvsAuthDto(BaseModel):
    """avs address model"""
    address: FlwBillingAddressDto

class FlwBillingAddressDto(BaseModel):
    """avs address data model"""
    city: str
    country: str
    line1: str
    line2: str
    postal_code: str
    state: str

class GeneratePaymentLinkDto(BaseModel):
   
    amount: int
    reference: str
    currency: str
    redirectUrl: str
    customization: Customization
    customer: Customer
    narration: str

class PaymentLinkDto(BaseModel):
    link: str

class PaymentLinkResponseDto(BaseModel):
    """payment link response model"""
    statusCode: int
    message: str 
    data: PaymentLinkDto
    errors: Optional[dict] = None

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

    

class StatusResponseDto(BaseModel):
    """authorize charge response model"""
    statusCode: int
    message: str 
    data: dict
    errors: Optional[str]=None

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)


class InitiateBankTransferDto(BaseModel):
    """bank transfer request model"""
    amount: int
    bank: str 
    accountNumber: str
    transactionPin: str
    reference:str
    narration:str
    meta: Dict

class InitiateBankTransferResponseDto(BaseModel):
    
    statusCode: int
    message: str 
    data: InitiateBankTransferResponseDataDto
    errors: dict

class InitiateBankTransferResponseDataDto(BaseModel):
    
    reference: str
    status: PaymentStatus
    amount: int 

class PeerTransferResponseDto(BaseModel):
    """p2p transfer response model"""
    statusCode: int
    message: str 
    data: Any
    error: Optional[str]=None

class PeerTransferDto(BaseModel):
    """p2p transfer request model"""
    receiver: str
    amount: int
    transactionPin: str
    currency: Optional[str]

class VerifyBankAccountRequestDto(BaseModel):
    """verify bank request model"""

    accountNumber: str
    bank: str

class VerifyBankResponseDto(BaseModel):
    statusCode: int
    message: str 
    data: VerifyBankAccountDto
    errors: Optional[dict] = None

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

class VerifyBankAccountDto(BaseModel):
    accountNumber: str
    accountName: str
    bankCode: str
    bankName: str

class BankAccountResponseDto(BaseModel):
    
    statusCode: int
    message: str 
    data: BankAccountDto
    errors:Optional[dict] = None

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)



class NairaBalanceDto(BaseModel):
    id: str
    createdAt: datetime
    updatedAt: datetime
    deletedDate: Optional[datetime]

    parentWalletId: str
    type: Literal["FIAT", "CRYPTO"]
    currency: str
    balance: float

    chain: Optional[str]
    publicAddress: Optional[str]

    virtualAccount: Optional[VirtualAccountDto]
    evmPortfolio: Optional[Dict[str, Any]]
    solPortfolio: Optional[Dict[str, Any]]

class NairaBalanceResponseDto(BaseModel):
    statusCode: int
    message: str
    data: NairaBalanceDto
    errors: Optional[Dict[str, Any]]

