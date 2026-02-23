"""Wallet service implementation"""

from typing import Dict, Any, List, Optional
from ...models.offramp import (
    OfframpTransactionListResponseDto,OfframpStatusRequestDto,OfframpTransactionDetailResponseDto
)
from ...exceptions import MoneiAPIError


class OfframpLedgerService:
    """Ledger Service for Offramp operations"""
    
    def __init__(self, client):
        self.client = client
    
    async def get_offramp_transactions(self) -> OfframpTransactionListResponseDto:
        """Get transaction history."""
 
        response = await self.client._request("GET", "/offramp/ledger/history")
        return response
    
    async def offramp_transaction_status(self, request:OfframpStatusRequestDto) -> OfframpTransactionDetailResponseDto:
        """Get Crypto-to-Fiat quote."""
 
        response = await self.client._request("GET", "/offramp/ledger/status/reference", data=request.dict())
        return OfframpTransactionDetailResponseDto(**response)
    
  
   