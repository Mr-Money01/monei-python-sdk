"""Wallet service implementation"""

from typing import Dict, Any, List, Optional
from ...models.wallet import (
    InitiateBankTransferDto, InitiateBankTransferResponseDto,PeerTransferDto,PeerTransferResponseDto

)
from ...exceptions import MoneiAPIError


class WalletPayoutService:
    """Payout Service for wallet operations"""
    
    def __init__(self, client):
        self.client = client
    
    async def bank_transfer(self, request:InitiateBankTransferDto) -> InitiateBankTransferResponseDto:
        """make a transfer to another bank"""
 
        response = await self.client._request("POST", "/wallet/payout/bank-transfer", data=request.dict())
        return InitiateBankTransferResponseDto(**response)
    
    async def peer_transfer(self, request:PeerTransferDto) -> PeerTransferResponseDto:
        """internal transfer to another user """
        response = await self.client._request(
            "POST", "/wallet/payout/transfer", data=request.dict()
        )
        return PeerTransferResponseDto(**response)
    
   