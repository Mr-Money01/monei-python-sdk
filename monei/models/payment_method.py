"""Payment method related models"""

from typing import Dict,Optional,Any
from .base import BaseDto
from pydantic import BaseModel
from .enums.payment_method import PaymentMethodType
    

class PaymentMethodDto(BaseModel):
    """Payment method details model"""
    id: str
    type: str
    status: str
    isDefault: bool
    nickname: str
    isEnabled: bool
    lastUsedAt:str
    usageCount: str
    capabilities: str
    details: str
    createdAt: str
    updatedAt: str

class SyncPaymentMethodsDto(BaseModel):
    """synn payment model"""
    subWalletId: str

class CreatePaymentMethodDto(BaseModel):
    """Payment method request model"""
    type: PaymentMethodType
    nickname: str
    subWalletId: str
    card: AddCardDto
    virtualAccountId: str
    ussd: AddUssdDto

class AddUssdDto(BaseModel):
    bankCode: str

class AddCardDto(BaseModel):
    expiryMonth: str
    expiryYear: str
    cardNumber: str
    cvv: str
    cardHolderName: str



class PaymentMethodResponseDto(BaseModel):
    """payment method response model"""
    statusCode: int
    message: str 
    data:PaymentMethodDto
    errors: Optional[Dict[str, Any]] = None

class PaymentMethodsResponseDto(BaseModel):
    """payment method response model"""
    statusCode: int
    message: str 
    data: Dict[str, PaymentMethodDto]
    errors: Optional[Dict[str, Any]] = None

class DeletePaymentMethodResponseDto(BaseModel):
    """payment method response model"""
    statusCode: int
    message: str 
    data: PaymentMethodDto
    errors:Optional[Dict[str, Any]] = None


