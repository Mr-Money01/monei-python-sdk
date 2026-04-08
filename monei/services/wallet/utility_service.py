"""Wallet service implementation"""

from typing import Dict, Any, List, Optional
from ...models.wallet import (
   VerifyBankResponseDto,
    VerifyBankAccountRequestDto,BankListResponseDto,BankAccountResponseDto
)
from ...exceptions import MoneiAPIError


class WalletUtilityService:
    """Service for wallet operations"""
    
    def __init__(self, client):
        self.client = client
    
    
    async def get_banks(self) -> BankListResponseDto:
        """Get available banks"""
        response = await self.client._request("GET", "/wallet/utils/banks")

        #banks = response["data"]
        #return [BankDto(**bank) for bank in banks]
        return BankListResponseDto(**response)
    
    async def verify_bank_account(self, request:VerifyBankAccountRequestDto) -> BankAccountResponseDto:
        """Verify bank account"""
        
        response = await self.client._request(
            "POST", "/wallet/utils/verify-bank-account", data=request.dict()
        )
        
        return BankAccountResponseDto(**response)