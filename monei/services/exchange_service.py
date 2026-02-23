"""Exchange service"""

from ..models.exchange import (
    PriceResponseDto, SwapNativeToTokenDto, SwapTokenToTokenDto, SwapTokenToNativeDto,
    SwapSolToTokenDto, ZeroExQuoteDto, SwapDto, TxHashDto
)


class ExchangeService:
    """Service for exchange operations"""
    
    def __init__(self, client):
        self.client = client
    
    # EVM Exchange
    async def get_swap_native_to_token_price(self, request: SwapNativeToTokenDto) -> PriceResponseDto:
        """Get price for native to token swap"""
        response = await self.client._request(
            "POST", "/evm-exchange/price/native-to-token", data=request.dict()
        )
        return PriceResponseDto(amount=response['data']['toAmount'])
    
    async def swap_native_to_token(self, request: SwapNativeToTokenDto) -> TxHashDto:
        """Swap native to token"""
        response = await self.client._request(
            "POST", "/evm-exchange/native-to-token", data=request.dict()
        )
        return TxHashDto(**response['data'])
    
    async def get_swap_token_to_token_price(self, request: SwapTokenToTokenDto) -> PriceResponseDto:
        """Get price for token to token swap"""
        response = await self.client._request(
            "POST", "/evm-exchange/price/token-to-token", data=request.dict()
        )
        return PriceResponseDto(amount=response['data']['toAmount'])
    
    async def swap_token_to_token(self, request: SwapTokenToTokenDto) -> TxHashDto:
        """Swap token to token"""
        response = await self.client._request(
            "POST", "/evm-exchange/token-to-token", data=request.dict()
        )
        return TxHashDto(**response['data'])

    async def get_swap_token_to_native_price(self, request: SwapTokenToTokenDto) -> PriceResponseDto:
        """Get price for token to native swap"""
        response = await self.client._request(
            "POST", "/evm-exchange/price/token-to-native", data=request.dict()
        )
        return PriceResponseDto(amount=response['data']['toAmount'])
    
    async def swap_token_to_native(self, request: SwapTokenToTokenDto) -> TxHashDto:
        """Swap token to native"""
        response = await self.client._request(
            "POST", "/evm-exchange/token-to-native", data=request.dict()
        )
        return TxHashDto(**response['data'])
    
    # Solana Exchange
   
    
    async def get_token_to_sol_quote(self, input_mint: str, amount: float) -> dict:
        """Get Solana swap quote"""
        params = {
            'inputMint': input_mint, 
            'amount': amount
        }
        response = await self.client._request("GET", "/solana-exchange/quote/token-to-sol", params=params)
        return response
    
    async def get_sol_to_token_quote(self, input_mint: str, amount: float) -> dict:
        """Get Solana swap quote"""
        params = {
            'outputMint': input_mint, 
            'amount': amount
        }
        response = await self.client._request("GET", "/solana-exchange/quote/sol-to-token", params=params)
        return response

    async def get_token_to_token_quote(self, input_mint: str, output_mint: str, amount: float) -> dict:
        """Get Solana swap quote"""
        params = {
            'inputMint': input_mint, 
            'outputMint': output_mint,
            'amount': amount
        }
        response = await self.client._request("GET", "/solana-exchange/quote/token-to-token", params=params)
        return response
    
    async def swap_sol_to_token(self, request: SwapSolToTokenDto) -> SwapDto:
        """Swap SOL to token"""
        response = await self.client._request(
            "POST", "/solana-exchange/swap-sol-to-token", data=request.dict()
        )
        return SwapDto(**response['data'])
    
    async def swap_token_to_token_solana(self, request: SwapTokenToTokenDto) -> SwapDto:
        """Swap token to token on Solana"""
        response = await self.client._request(
            "POST", "/solana-exchange/swap-token-to-token", data=request.dict()
        )
        return SwapDto(**response['data'])
    
    async def swap_token_to_sol(self, request: SwapSolToTokenDto) -> SwapDto:
        """Swap token to SOL"""
        response = await self.client._request(
            "POST", "/solana-exchange/swap-token-to-sol", data=request.dict()
        )
        return SwapDto(**response['data'])