"""Wallet-related models"""


from typing import Optional, Literal, Dict, Any,List
from pydantic import BaseModel
from datetime import datetime
from .base import BaseDto
from enum import Enum
from .enums.wallet import PaymentStatus, NextActionType, DepositAuthType
    

class SubWalletDto(BaseDto):
    """Sub-wallet model"""
    parentWalletId: Optional[str] = None  # Make optional
    type: str  # "FIAT" or "CRYPTO"
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
    errors:dict

class GetNairaWalletResponseDto(BaseModel):
    """naira wallet details response model"""
    statusCode: int
    message: str 
    data: BankAccountDto

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
    swiftCode: Optional[str] = None
    bic: Optional[str] = None
    isMobileVerified: Optional[bool] = None
    isCashPickUp: Optional[bool] = None
    nibssCode: Optional[str] = None
    id: int
    code: str
    name: str
    branches: Optional[List[List[Any]]] = []

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
    errors: dict

class VerifyBankResponseDto(BaseModel):
    """verify bank response model"""
    statusCode: int
    message: str 
    data: BankAccountDto

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

class VirtualAccountResponseDto(BaseModel):
    """virtual account response model"""
    statusCode: int
    message: str 
    data: VirtualAccountDto
    errors:dict

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
    reference:int
    currency:int
    redirectUrl:str
    customization: Customization
    customer: Customer
    narration:str
    accountNumber:str
    bankName:str
    accountName:str
    expiry_datetime:str
    note:str
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

class PaymentResponseDto(BaseModel):
    """payment response model"""
    statusCode: int
    message: str 
    data: PaymentDto
    errors: dict

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
    pin: str
    otp: str
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
    errors: dict

class StatusResponseDto(BaseModel):
    """authorize charge response model"""
    statusCode: int
    message: str 
    data: dict
    errors: Optional[str]=None

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

class BankAccountResponseDto(BaseModel):
    
    statusCode: int
    message: str 
    data: BankAccountDto
    errors:dict

class BankAccountDto(BaseModel):
    accountName:str
    accountNumber:str
    bankCode:str
    bankName:str

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

