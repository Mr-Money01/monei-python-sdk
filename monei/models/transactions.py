"""Transaction models"""

from typing import Optional
from datetime import datetime
from .base import BaseDto

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