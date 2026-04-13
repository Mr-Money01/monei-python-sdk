"""Solana wallet service"""

from typing import Optional
from ..models.solana import (
    AddressDto, BalanceResponseDto, PortfolioDto, SignatureResponseDto, TransferSolDto,
    TransferTokenDto, SignatureDto, SolanaNetwork,WalletAddressResponseDto,PortfolioResponseDto
)


class SolanaService:
    """Service for Solana wallet operations"""
    
    def __init__(self, client):
        self.client = client
    
    async def get_address(self) -> WalletAddressResponseDto:
        """Get Solana wallet address"""
        response = await self.client._request("GET", "/solana/address")
        return response
    
    async def get_native_balance(self, network: Optional[SolanaNetwork] = None) -> BalanceResponseDto:
        """Get SOL balance"""
        params = {}
        if network:
            params['network'] = network.value
            
        response = await self.client._request("GET", "/solana/balance", params=params)
        return BalanceResponseDto(**response)
    
    async def get_token_balance(self, token_mint_address: str, network: Optional[SolanaNetwork] = None) -> BalanceResponseDto:
        """Get token balance"""
        params = {}
        if network:
            params['network'] = network.value
            
        response = await self.client._request(
            "GET", f"/solana/token-balance/{token_mint_address}", params=params
        )
        return BalanceResponseDto(**response)
    
    async def get_portfolio(self, network: Optional[SolanaNetwork] = None) -> PortfolioResponseDto:
        """Get Solana portfolio"""
        params = {}
        if network:
            params['network'] = network.value
            
        response = await self.client._request("GET", "/solana/portfolio", params=params)
        return PortfolioResponseDto(**response)
    
    async def send_native_token(self, request: TransferSolDto) -> SignatureResponseDto:
        """Transfer SOL"""
        response = await self.client._request(
            "POST", "/solana/transfer", data=request.dict()
        )
        return SignatureResponseDto(**response)
    
    async def send_token(self, request: TransferTokenDto) -> SignatureResponseDto:
        """Transfer SPL token"""
        response = await self.client._request(
            "POST", "/solana/transfer-token", data=request.dict()
        )
        return SignatureResponseDto(**response)