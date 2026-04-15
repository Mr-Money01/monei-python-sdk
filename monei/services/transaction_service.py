"""Transaction service"""

from typing import List, Optional, Dict, Any
from ..models.transactions import TransactionResponseDto, TransactionDto
from ..models.transactions import UserTransactionsResponseDto, TransactionsRequestDto, PaginationDto
from ..models.enums.transactions import TransactionType, TransactionStatus 

class TransactionService:
    """Service for transaction operations"""
    
    def __init__(self, client):
        self.client = client
    
    async def get_all(self, request_data: Optional[TransactionsRequestDto] = None) -> UserTransactionsResponseDto:
        """Get all user transactions"""
        params = request_data.dict() if request_data else {}
        response = await self.client._request("GET", "/transactions/user", params=params)
        return UserTransactionsResponseDto(**response)
    
    async def get_transactions_by_type(self, type: TransactionType, request_data: TransactionsRequestDto) -> Dict[str, Any]:
        """Get transactions filtered by type"""
        response = await self.get_all(request_data)
        
        filtered_transactions = [
            t for t in response.data 
            if t.type == type
        ]
        
        return {
            "transactions": filtered_transactions,
            "pagination": response.pagination
        }
    
    async def get_deposits(self) -> TransactionDto:
        """Get all deposit transactions"""
        
        return await self.get_transactions_by_type(TransactionType.CREDIT, TransactionsRequestDto())
    
    async def get_deposit(self, **kwargs) -> TransactionDto:
        """Get a single deposit by either ID or reference"""
        if 'id' in kwargs:
            return await self.get_by_id(kwargs['id'])
        elif 'reference' in kwargs:
            return await self.get_by_reference(kwargs['reference'])
        else:
            raise ValueError("Either 'id' or 'reference' must be provided")
    
    async def get_by_id(self, id: str) -> TransactionDto:
        """Get transaction by ID"""
        response = await self.client._request("GET", f"/transactions/{id}")
        return response
    
    async def get_by_reference(self, reference: str) -> TransactionDto:
        """Get transaction by reference"""
        response = await self.client._request("GET", f"/transactions/reference/{reference}")
        return response
