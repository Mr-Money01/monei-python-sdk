"""Wallet service implementation"""

from typing import Dict, Any, List, Optional
from ...models.offramp import (
   AssetsResponseDto,OfframpExchangeRateDto,SwapCryptoToFiatRequestDto,OfframpOrderResponseDto
)
from ...exceptions import MoneiAPIError


class OfframpExchangeService:
    """Exchange Service for Offramp operations"""
    
    def __init__(self, client):
        self.client = client
    
    async def get_assets(self) -> AssetsResponseDto:
        """Retrieve all supported Crypto-Network pairs."""
 
        response = await self.client._request("GET", "/offramp/exchange/assets")
        return response
    
    async def get_quote(self, request:OfframpExchangeRateDto) -> dict:
        """Get Crypto-to-Fiat quote."""
        #response = await self.client._request("GET", "/offramp/exchange/quote", data=request.dict())
        response = await self.client._request(
            "GET",
            "/offramp/exchange/quote",
            params=request.model_dump()
        )
        return response
    
    async def initiate_swap(self, request:SwapCryptoToFiatRequestDto) -> OfframpOrderResponseDto:
        """initiate a Crypto-to-Fiat order"""
        response = await self.client._request(
            "POST", "/offramp/exchange/initiate", data=request.dict()
        )
        return OfframpOrderResponseDto(**response)
    
   