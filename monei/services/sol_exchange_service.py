"""Exchange service"""

from ..models.exchange import (
     SwapQuoteResponseDto,
     SwapResponseDto,
     SwapTokenToTokenDto, 
    SwapSolToTokenDto,  SwapDto
)


class SolanaExchangeService:
    """Service for exchange operations"""
    
    def __init__(self, client):
        self.client = client
    
    
    
    # Solana Exchange
   
    
    async def get_token_to_sol_quote(self, input_mint: str, amount: float) -> SwapQuoteResponseDto:
        """Get Solana swap quote"""
        params = {
            'inputMint': input_mint, 
            'amount': amount
        }
        response = await self.client._request("GET", "/solana-exchange/quote/token-to-sol", params=params)
        return SwapQuoteResponseDto(**response)
    
    async def get_sol_to_token_quote(self, input_mint: str, amount: float) -> SwapQuoteResponseDto:
        """Get Solana swap quote"""
        params = {
            'outputMint': input_mint, 
            'amount': amount
        }
        response = await self.client._request("GET", "/solana-exchange/quote/sol-to-token", params=params)
        return SwapQuoteResponseDto(**response)

    async def get_token_to_token_quote(self, input_mint: str, output_mint: str, amount: float) -> SwapQuoteResponseDto:
        """Get Solana swap quote"""
        params = {
            'inputMint': input_mint, 
            'outputMint': output_mint,
            'amount': amount
        }
        response = await self.client._request("GET", "/solana-exchange/quote/token-to-token", params=params)
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
    
    async def swap_token_to_sol(self, request: SwapSolToTokenDto) -> SwapResponseDto:
        """Swap token to SOL"""
        response = await self.client._request(
            "POST", "/solana-exchange/swap-token-to-sol", data=request.dict()
        )
        return SwapResponseDto(**response)