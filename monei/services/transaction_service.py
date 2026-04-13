"""Transaction service"""

from typing import List, Optional
from ..models.transactions import TransactionResponseDto, TransactionDto


class TransactionService:
    """Service for transaction operations"""
    
    def __init__(self, client):
        self.client = client
    
    async def get_all(self) -> List[TransactionResponseDto]:
        """Get user transactions"""
        response = await self.client._request("GET", "/transactions/user")
        #print(response)
        return [TransactionResponseDto(**tx) for tx in response['data']['transactions']]
    
    async def get_transaction(self, transaction_id: str) -> TransactionDto:
        """Get transaction by ID"""
        response = await self.client._request("GET", f"/transactions/{transaction_id}")
        print(response)
        #return TransactionDto(**response['data'])
        return TransactionDto(**response)
    
    async def get_transaction_by_reference(self, reference: str) -> TransactionDto:
        """Get transaction by reference"""
        response = await self.client._request("GET", f"/transactions/reference/{reference}")
        return TransactionDto(**response)