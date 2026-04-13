"""Exchange service"""

from ..models.exchange import (
    SwapNativeToTokenDto, SwapPriceResponseDto, SwapTokenToTokenDto, TxHashResponseDto
)


class EvmExchangeService:
    """Service for exchange operations"""
    
    def __init__(self, client):
        self.client = client
    
    # EVM Exchange
    async def get_native_to_token_price(self, request: SwapNativeToTokenDto) -> SwapPriceResponseDto:
        """Get price for native to token swap"""
        response = await self.client._request(
            "POST", "/evm-exchange/price/native-to-token", data=request.dict()
        )
        #return PriceResponseDto(amount=response['data']['toAmount'])
        return  SwapPriceResponseDto(**response)
    
    async def swap_native_to_token(self, request: SwapNativeToTokenDto) ->  TxHashResponseDto:
        """Swap native to token"""
        response = await self.client._request(
            "POST", "/evm-exchange/native-to-token", data=request.dict()
        )
        #return TxHashDto(**response['data'])
        return TxHashResponseDto(**response)
    
    async def get_token_to_token_price(self, request: SwapTokenToTokenDto) -> SwapPriceResponseDto:
        """Get price for token to token swap"""
        response = await self.client._request(
            "POST", "/evm-exchange/price/token-to-token", data=request.dict()
        )
        #return PriceResponseDto(amount=response['data']['toAmount'])
        return SwapPriceResponseDto(**response)
    
    async def swap_token_to_token(self, request: SwapTokenToTokenDto) -> TxHashResponseDto:
        """Swap token to token"""
        response = await self.client._request(
            "POST", "/evm-exchange/token-to-token", data=request.dict()
        )
        #return TxHashDto(**response['data'])
        return TxHashResponseDto(**response)

    async def get_token_to_native_price(self, request: SwapTokenToTokenDto) -> SwapPriceResponseDto:
        """Get price for token to native swap"""
        response = await self.client._request(
            "POST", "/evm-exchange/price/token-to-native", data=request.dict()
        )
        #return PriceResponseDto(amount=response['data']['toAmount'])
        return SwapPriceResponseDto(**response)
    
    async def swap_token_to_native(self, request: SwapTokenToTokenDto) -> TxHashResponseDto:
        """Swap token to native"""
        response = await self.client._request(
            "POST", "/evm-exchange/token-to-native", data=request.dict()
        )
        #return TxHashDto(**response['data'])
        return TxHashResponseDto(**response)

    