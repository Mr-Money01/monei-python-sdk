"""Payment method related models"""

from typing import Dict, List,Optional,Any
from .base import BaseDto
from pydantic import BaseModel
from .enums.payment_method import PaymentMethodType
    

class Capabilities(BaseModel):
    """Capabilities model"""
    canReceive: bool
    canSend: bool
    maxSingleAmount: int
    dailyLimit: int
    monthlyLimit: int

class PaymentMethodDetailsDto(BaseModel):
    """Payment method details model"""
    id: str
    type: str
    status: str
    isDefault: bool
    nickname: str
    isEnabled: bool
    lastUsedAt: Optional[str] = None  # Can be None
    usageCount: int  # Should be int, not str
    capabilities: Capabilities  # Nested object, not string
    details: Dict[str, Any]  # Empty dict in response
    createdAt: str  # Or use datetime
    updatedAt: str  # Or use datetime

class PaymentMethodDto(BaseModel):
    """Payment method model"""
    
    type: PaymentMethodType
    nickname: Optional[str] = None
    subWalletId: str
    card: Optional[AddCardDto] = None
    virtualAccountId: Optional[str] = None
    ussd: Optional[AddUssdDto] = None
   
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
    data:PaymentMethodDetailsDto
    errors: Optional[Dict[str, Any]] = None

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

class PaymentMethodsResponseDto(BaseModel):
    """payment method response model"""
    statusCode: int
    message: str 
    data: List[PaymentMethodDetailsDto]  
    errors: Optional[Dict[str, Any]] = None

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

class DeletePaymentMethodResponseDto(BaseModel):
    """payment method response model"""
    statusCode: int
    message: str 
    data: Optional[Dict[str, Any]] = None  
    errors:Optional[Dict[str, Any]] = None

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)


