"""offramp operation related models"""

from typing import Optional
from enum import Enum
from .base import BaseDto
from typing import List, Optional, Dict, Any
from pydantic import BaseModel
from .enums.offramp import OfframpStatus,WalletType,OfframpCurrency, Providers, OfframpAssets,OfframpNetworks
    

class OframpQuoteRequestDto(BaseModel):
  token: OfframpAssets
  network: OfframpNetworks
  amount: int
  fiat: Optional[OfframpCurrency]=None

class AssetsResponseDto(BaseModel):
    statusCode: int
    message: str
    data: list
    errors:Optional[Dict[str, Any]] = None
    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

class OfframpExchangeRateDto(BaseModel):
    token: str
    network: str
    amount: int
    fiat: Optional[str]=None
    rate: Optional[int] = None

class OframpQuoteResponseDto(BaseModel):
    statusCode: int
    message: str
    data: OfframpExchangeRateDto
    errors:Optional[Dict[str, Any]] = None
    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

class SwapCryptoToFiatRequestDto(BaseModel):
    amount: int
    token: str
    network: str
    fiatCurrency: str
    bankCode: str
    accountNumber: str
    accountName: str

class CryptoAmountDto(BaseModel):
  value: int
  asset: OfframpAssets
  network: OfframpNetworks
  
class FiatAmountDto(BaseModel):
  value: int
  currency: OfframpCurrency
  
class AmountsDto(BaseModel):
  crypto: CryptoAmountDto
  fiat: FiatAmountDto
  exchangeRate: int
  totalFee: int

class BeneficiaryDto(BaseModel):
  bankCode: str
  bankName: str
  accountNumber: int
  accountName: str

class OnChainDto(BaseModel):
  depositAddress: str
  txHash: str
  sourceWallet: WalletType

class TimestampsDto(BaseModel):
  created: str
  updated: str
  completed:Optional[str]=None
  failed: Optional[str]=None
  depositDetected:Optional[str]=None
  depositConfirmed:Optional[str]=None
  depositExpires: Optional[str]=None
  
class OfframpOrderResponseDataDto(BaseModel):
    id:str
    reference:str
    status: OfframpStatus
    amounts: AmountsDto
    beneficiary:BeneficiaryDto
    onChain:OnChainDto
    #provider: Providers
    #providerReference:str
    meta:Optional[Dict[str, Any]] = None
    failureReason: Optional[str]=None
    timestamps:TimestampsDto

class OfframpOrderResponseDto(BaseModel):
    statusCode: int
    message: str
    data: OfframpOrderResponseDataDto
    errors:Optional[Dict[str, Any]] = None

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

class PayoutBankDto(BaseModel):
    name: str
    code: str
   
class PayoutBanksResponseDto(BaseModel):
    statusCode: int
    message: str
    data: list[PayoutBankDto]
    errors:Optional[Dict[str, Any]] = None
    
    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

class VerifyOfframpBankAccountResponseDataDto(BaseModel):
    bankCode: int
    bankName: str
    accountNumber:str
    accountName:str 

class VerifyOfframpBankAccountResponseDto(BaseModel):
    statusCode: int
    message: str
    data: VerifyOfframpBankAccountRequestDto
    errors:Optional[Dict[str, Any]] = None

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

class VerifyOfframpBankAccountRequestDto(BaseModel):
    bankCode: str
    accountNumber: str

class OfframpHistoryRequestDto(BaseModel):
    limit: Optional[str]=None
    page: Optional[str]=None

class OfframpTransactionResponseDto(BaseModel):
    id: str
    internalReference: str
    provider: str
    providerTransactionId:str
    status:OfframpStatus
    cryptoAmount:int
    fiatAmount:int
    exchangeRate:int
    fromCurrency:str
    toCurrency:str
    createdAt:str
    updatedAt:str
    expiresAt:str

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

class MetaDto(BaseDto):
    currentPage: int
    itemsPerPage: int
    totalItems: int
    totalPages: int

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

class OfframpTransactionListResponseDto(BaseModel):
    ststusCode:int
    message:str
    data:list[OfframpTransactionResponseDto]
    meta:Optional[MetaDto] = None

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

class OfframpTransactionDetailResponseDto(BaseModel):
    id: str
    internalReference: str
    provider: str
    providerTransactionId:str
    status:OfframpStatus
    cryptoAmount:int
    fiatAmount:int
    exchangeRate:int
    fromCurrency:str
    toCurrency:str
    createdAt:str
    updatedAt:str
    expiresAt:str
    providerStatus:str
    fees:Optional[Dict[str, Any]] = None
    debitPaymentDetails:Optional[Dict[str, Any]] = None
    creditPaymentDetails:Optional[Dict[str, Any]] = None
    completedAt:str

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

class OfframpStatusRequestDto(BaseModel):
    reference: str
