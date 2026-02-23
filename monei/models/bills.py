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


class ElectricityBillerDto(BaseModel):
    """Electricity biller information"""
    name: str
    code: str
    billerCode: str
    
class ElectricityBillerResponseDto(BaseModel):
    """Electricity biller information"""
    statusCode: int
    message: str 
    data: List[ElectricityBillerDto]
    errors:Optional[Dict[str, Any]] = None

class BillerItemsResponse(BaseModel):
    """"""
    statusCode: int
    message: str 
    data: List[BillerDto]
    errors:Optional[Dict[str, Any]] = None

class ValidateBillDto(BaseModel):
    """Validate bill request"""
    billlerCode:str
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
    isSchedule: bool = Optional[False]
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
    isSchedule: bool = False
    scheduleData: Optional[CreateBillScheduleDto] = None
    saveBeneficiary: bool = False
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
    data: List[BillPaymentDto]
    errors:Optional[Dict[str, Any]] = None

class BillDto(BaseDto):
    """Bill history item"""
    userId: str
    reference: str
    billerCode: str
    itemCode: str
    customer: str
    amount: float
    type: BillCategory
    status: str
    txRef: str
    billerName: str
    validityPeriod: Optional[str] = None
    metadata: Optional[str] = None
    token: Optional[str] = None
    units: Optional[str] = None

class BillHistoryDto(BaseModel):
    """Bill history item"""
    bills: List[BillDto]
    page: int
    limit: int
    total: int
    totalPages: int
    hasNextt: bool
    hasPrev:bool

class BillHistoryResponseDto(BaseModel):
    """Bill history response"""
    statusCode: int
    message: str
    data: BillHistoryDto
    errors:Optional[Dict[str, Any]] = None

class BillResponseDto(BaseModel):
    statusCode:int
    message: str
    data: BillDto
    errors:Optional[Dict[str, Any]] = None

class BillNotFoundResponseDto(BaseModel):
    success:bool
    message: str
    errorCode:str
    reference:str