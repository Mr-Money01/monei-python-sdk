"""Wallet service implementation"""

from typing import Dict, Any, List, Optional
from ...models.wallet import (
    UserWalletDto, NairaBalanceResponseDto, CreateVirtualAccountDto, VirtualAccountResponseDto
)
from ...exceptions import MoneiAPIError


class WalletAccountService:
    """Account Service for wallet operations"""
    
    def __init__(self, client):
        self.client = client
    
    async def get_wallet(self, chain_id: Optional[int] = None) -> UserWalletDto:
        """Get wallet information"""
        params = {}
        if chain_id:
            params['chainId'] = chain_id
            
        response = await self.client._request("GET", "/wallet/me", params=params)
        return UserWalletDto(**response)
    
    async def get_naira_wallet(self) -> NairaBalanceResponseDto:
        """Get naira wallet information"""

        response = await self.client._request("GET", "/wallet/naira-wallet")
        return NairaBalanceResponseDto(**response)
    
    async def create_virtual_account(self, request:CreateVirtualAccountDto) -> VirtualAccountResponseDto:
        """create a virtual account for a user"""
       
        response = await self.client._request(
            "POST", "/wallet/virtual-account", data=request.dict()
        )
        return VirtualAccountResponseDto(**response)
    
    