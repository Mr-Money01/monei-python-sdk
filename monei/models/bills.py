"""Bill payment models"""

from typing import Optional, List,Any,Dict
from datetime import datetime
from enum import Enum
from .base import BaseDto, BaseModel
from .enums.bills import BillCategory

class BillerDto(BaseModel):
    """Biller information"""
    id: int
    biller_code: str
    name: str
    default_commission: float
    date_added: str
    country: str
    is_airtime: bool
    biller_name: str
    item_code: str
    short_name: str
    fee: float
    commission_on_fee: bool
    reg_expression: str
    label_name: str
    amount: float
    is_resolvable: bool
    group_name: str
    category_name: str
    is_data: Optional[bool] = None
    default_commission_on_amount: Optional[float] = None
    commission_on_fee_or_amount: Optional[int] = None
    validity_period: Optional[str] = None

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)


class ElectricityBillerDto(BaseModel):
    """Electricity biller information"""
    name: str
    code: str
    billerCode: str
    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)
    
class ElectricityBillerResponseDto(BaseModel):
    """Electricity biller information"""
    StatusCode: int
    message: str 
    data: List[ElectricityBillerDto]
    errors:Optional[Dict[str, Any]] = None

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)
    

class BillerItemsResponseDto(BaseModel):
    """"""
    statusCode: int
    message: str 
    data: List[BillerDto]
    errors:Optional[Dict[str, Any]] = None
    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

class ValidateBillDto(BaseModel):
    """Validate bill request"""
    billerCode:str
    itemCode: str
    customer: str
    

class CreateBillScheduleDto(BaseModel):
    """Bill schedule request"""
    executionDate: datetime
    isRecurring: bool = False
    recurrencePattern: Optional[str] = None

class AirtimePurchaseDto(BaseModel):
    """Airtime purchase request"""
    phoneNumber: str
    biller: str
    amount: float
    isSchedule: Optional[bool] = False
    scheduleData: Optional[CreateBillScheduleDto] = None
    saveBeneficiary: bool = False
    beneficiaryName: Optional[str] = None

class DataPurchaseDto(BaseModel):
    """Data purchase request"""
    phoneNumber: str
    biller: str
    itemCode: str
    isSchedule: bool = False
    scheduleData: Optional[CreateBillScheduleDto] = None
    saveBeneficiary: bool = False
    beneficiaryName: Optional[str] = None

class ElectricityPaymentDto(BaseModel):
    """Electricity payment request"""
    meterNumber: str
    amount: float
    disco: str
    isSchedule: bool = False
    scheduleData: Optional[CreateBillScheduleDto] = None
    saveBeneficiary: bool = False
    beneficiaryName: Optional[str] = None

class CableTvPaymentDto(BaseModel):
    """Cable TV payment request"""
    smartcardNumber: str
    biller: str
    itemCode: str
    isSchedule: Optional[bool] = False
    scheduleData: Optional[CreateBillScheduleDto] = None
    saveBeneficiary: Optional[bool] = False
    beneficiaryName: Optional[str] = None

class BillPaymentDto(BaseModel):
    """Bill payment response"""
    id: str
    createdAt: str
    userId: str
    reference: str
    billerCode: str
    itemCode: str
    customer: str
    amount: float
    type: str
    status: str
    txRef: str
    billerName: str
    metadata: Optional[str] = None
    token: Optional[str] = None
    units: Optional[str] = None
    validityPeriod: Optional[str] = None

class BillPaymentResponseDto(BaseModel):
    """"""
    statusCode: int
    message: str 
    data: BillPaymentDto
    errors:Optional[Dict[str, Any]] = None
    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

class BillDto(BaseModel):
    """Bill history item"""
    id: str
    createdAt: str
    userId: str
    reference: str
    billerCode: str
    itemCode: str
    customer: str
    amount: str  # Keep as string since API returns string
    type: BillCategory  # Or use BillCategory if you want enum
    status: str
    txRef: str
    billerName: str
    validityPeriod: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None  # Changed to Dict for better compatibility
    token: Optional[str] = None
    units: Optional[str] = None
    
    def __contains__(self, key):
        return hasattr(self, key)

class BillHistoryDto(BaseModel):
    """Bill history item"""
    bills: List[BillDto]
    page: int
    limit: int
    total: int
    totalPages: int
    hasNext: bool
    hasPrev:bool

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

class BillHistoryResponseDto(BaseModel):
    """Bill history response"""
    statusCode: int
    message: str
    data: BillHistoryDto
    errors:Optional[Dict[str, Any]] = None
    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

class BillResponseDto(BaseModel):
    statusCode:int
    message: str
    data: BillDto
    errors:Optional[Dict[str, Any]] = None
    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

class BillNotFoundResponseDto(BaseModel):
    success:bool
    message: str
    errorCode:str
    reference:str

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)
    

class UserInfoDto(BaseModel):
    """User information"""
    id: str
    firstName: str
    lastName: str
    email: str

class MetadataDto(BaseModel):
    """Metadata information"""
    phoneNumber: str
    validityPeriod: Optional[str] = None
    dataPlan: Optional[str] = None

class BillTransactionResponseDto(BaseModel):
    """Transaction response DTO"""
    id: str
    reference: str
    type: str
    billerName: str
    customer: str
    amount: str  # Keeping as string since it has decimal places
    status: str
    createdAt: datetime
    updatedAt: datetime
    metadata: MetadataDto
    walletBalance: str
    providerData: Optional[Dict[str, Any]] = None
    user: UserInfoDto