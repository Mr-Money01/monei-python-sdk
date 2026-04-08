from typing import Dict, Any, List, Optional
from ...models.offramp import (
   PayoutBanksResponseDto,VerifyOfframpBankAccountRequestDto,VerifyOfframpBankAccountResponseDto
)
from ...exceptions import MoneiAPIError


class OfframpPayoutsService:
    """Exchange Service for Offramp operations"""
    
    def __init__(self, client):
        self.client = client
    
    async def get_banks(self) -> PayoutBanksResponseDto:
        """Get the lists of supported banks."""
        response = await self.client._request("GET", "/offramp/payouts/banks")
        return PayoutBanksResponseDto(**response)
    
    async def verify_bank_account(self, request:VerifyOfframpBankAccountRequestDto) -> VerifyOfframpBankAccountResponseDto:
        """Get Crypto-to-Fiat quote."""
        response = await self.client._request("POST", "/offramp/payouts/verify", data=request.dict())
        return VerifyOfframpBankAccountResponseDto(**response)
    
  
    
   