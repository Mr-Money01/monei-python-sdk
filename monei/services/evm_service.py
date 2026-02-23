"""EVM wallet service"""

from typing import Dict, Any
from ..models.evm import (
    BalanceDto, UserEvmPortfolioDto, SendNativeTokenDto,
    SendTokenDto, Response
)


class EvmService:
    """Service for EVM wallet operations"""
    
    def __init__(self, client):
        self.client = client
    
    async def get_native_balance(self, chain_id: int) -> Response:
        """Get native token balance"""
        params = {'chainId': chain_id}
        response = await self.client._request("GET", "/evm/balance/native", params=params)
        return Response.model_validate(response)
    
    async def get_token_balance(self, token_address: str, chain_id: int) -> Response:
        """Get ERC20 token balance"""
        params = {
            'tokenAddress': token_address,
            'chainId': chain_id
        }
        response = await self.client._request("GET", "/evm/balance/token", params=params)
        return Response.model_validate(response)

    async def get_portfolio(self, chain_id: int) -> Response:
        """Get EVM portfolio"""
        response = await self.client._request("GET", f"/evm/portfolio/{chain_id}")
        return Response.model_validate(response)

    async def get_supported_network(self) -> Response:
        """Get Supported Network"""
        response = await self.client._request("GET", f"/evm/networks")
        return Response.model_validate(response)
    
    async def send_native_token(self, request: SendNativeTokenDto) -> Response:
        """Send native token"""
        response = await self.client._request(
            "POST", "/evm/send/native", data=request.dict()
        )
        #return Response(**response['data'])
        return Response.model_validate(response)
    
    async def send_token(self, request: SendTokenDto) -> Response:
        """Send ERC20 token"""
        response = await self.client._request(
            "POST", "/evm/send/token", data=request.dict()
        )
        return Response.model_validate(response)