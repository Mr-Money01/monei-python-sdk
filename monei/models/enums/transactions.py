

from enum import Enum


class TransactionType(str, Enum):
    """Transaction type enum"""
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"
    #PEER-TRANSFER = "PEER-TRANSFER"



class TransactionStatus(str, Enum):
    """Transaction status enum"""
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"