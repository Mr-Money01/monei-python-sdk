"""Transaction models"""

from .base import BaseModel
from typing import Any, Dict,  Any, Optional
from datetime import datetime
from xml.parsers.expat import errors
from .base import BaseDto
from .enums.transactions import TransactionType, TransactionStatus

class TransactionResponseDto(BaseDto):
    """Transaction response"""
    userId: str
    amount: float
    type: str
    status: str
    reference: Optional[str] = None
    currency: Optional[str] = None
    narration: str

class TransactionDto(BaseDto):
    """Detailed transaction"""
    user: dict
    wallet: Optional[dict] = None
    subwallet: Optional[dict] = None
    amount: float
    type: str
    status: str
    currency: Optional[str] = None
    reference: Optional[str] = None
    fincraReference: Optional[str] = None
    narration: str
    metadata: Optional[dict] = None

class UserTransactionsResponseDto(BaseModel):
    """User transaction response"""
    statusCode: int
    message: str
    data: list[UserTransactionsDataDto]
    pagination: PaginationDto
    errors: Optional[Dict[str, Any]] = None

class UserTransactionsDataDto(BaseModel):
    """User transactions data"""
    transactions: list[TransactionResponseDto]
    
class PaginationDto(BaseModel):
    """Pagination details"""
    page: int
    limit: int
    total: int
    hasNextPage: bool
    hasPreviousPage: bool

class TransactionsRequestDto(BaseModel):
    """Request DTO for fetching transactions with pagination and filters"""
    page: Optional[int] = 1
    limit: Optional[int] = 20
    type: Optional[str] = None
    status: Optional[str] = None
    fromDate: Optional[datetime] = None
    toDate: Optional[datetime] = None

class TransactionResponseDto(BaseModel):
    """Transaction response DTO"""
    id: str
    userId: str
    amount: float
    type: TransactionType
    status: TransactionStatus
    reference: str
    currency: str
    narration: str
    createdAt: str
    updatedAt: str
    deletedDate: Optional[str] = None
    