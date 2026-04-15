"""Exchange service"""

from ..models.exchange import (
     SwapQuoteResponseDto,
     SwapResponseDto,
     SwapTokenToTokenDto, 
     SwapSolToTokenDto,  SwapDto,SwapTokenToSolDto
)


class SolanaExchangeService:
    """Service for exchange operations"""
    
    def __init__(self, client):
        self.client = client
    
    
    
    # Solana Exchange
   
    
    async def get_token_to_sol_quote(self, request: SwapSolToTokenDto) -> SwapQuoteResponseDto:
        """Get Solana swap quote"""
        
        response = await self.client._request("GET", "/solana-exchange/quote/token-to-sol", params=request.dict())
        return SwapQuoteResponseDto(**response)
    
    async def get_sol_to_token_quote(self, request: SwapTokenToSolDto) -> SwapQuoteResponseDto:
        """Get Solana swap quote"""
        
        response = await self.client._request("GET", "/solana-exchange/quote/sol-to-token", params=request.dict())
        return SwapQuoteResponseDto(**response)

    async def get_token_to_token_quote(self, request: SwapTokenToTokenDto) -> SwapQuoteResponseDto:
        """Get Solana swap quote"""
        
        response = await self.client._request("GET", "/solana-exchange/quote/token-to-token", params=request.dict())
        return SwapQuoteResponseDto(**response)

    async def swap_sol_to_token(self, request: SwapSolToTokenDto) -> SwapResponseDto:
        """Swap SOL to token"""
        response = await self.client._request(
            "POST", "/solana-exchange/swap-sol-to-token", data=request.dict()
        )
        return SwapResponseDto(**response)
    
    async def swap_token_to_token_solana(self, request: SwapTokenToTokenDto) -> SwapResponseDto:
        """Swap token to token on Solana"""
        response = await self.client._request(
            "POST", "/solana-exchange/swap-token-to-token", data=request.dict()
        )
        return SwapResponseDto(**response)
    
    async def swap_token_to_sol(self, request: SwapTokenToSolDto) -> SwapResponseDto:
        """Swap token to SOL"""
        response = await self.client._request(
            "POST", "/solana-exchange/swap-token-to-sol", data=request.dict()
        )
        return SwapResponseDto(**response)