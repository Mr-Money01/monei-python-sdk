"""Wallet service implementation"""

from typing import Dict, Any, List, Optional
from ...models.wallet import (
    GetNairaWalletResponseDto, UserWalletDto,UserWalletResponseDto, NairaBalanceResponseDto, CreateVirtualAccountDto, VirtualAccountResponseDto
)
from ...exceptions import MoneiAPIError, ValidationError


class WalletAccountService:
    """Account Service for wallet operations"""
    
    def __init__(self, client):
        self.client = client
    
    async def me(self, chain_id: Optional[int] = None) -> UserWalletResponseDto:
        """Get wallet information"""
        params = {}
        if chain_id:
            params['chainId'] = chain_id
            
        response = await self.client._request("GET", "/wallet/me", params=params)
        return UserWalletResponseDto(**response)
    
    async def me(self) -> GetNairaWalletResponseDto:
        """Get naira wallet information"""

        response = await self.client._request("GET", "/wallet/naira-wallet")
        return GetNairaWalletResponseDto(**response)
    
    async def create_virtual_account(self, request: CreateVirtualAccountDto) -> VirtualAccountResponseDto:
        """create a virtual account for a user"""
        try:
            response = await self.client._request(
                "POST", "/wallet/virtual-account", data=request.dict()
            )
            return VirtualAccountResponseDto(**response)
        except ValidationError as e:
            # Parse error details if needed
            error_response = VirtualAccountResponseDto(
                statusCode=400,
                message="Validation error occurred",
                errors=e.errors if hasattr(e, 'errors') else [str(e)]
            )
            return error_response