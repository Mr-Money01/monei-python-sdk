"""Exchange models"""

from typing import Any, Dict, List, Optional
from .base import BaseModel

class SwapNativeToTokenDto(BaseModel):
    """Swap native to token request"""
    amount: str
    tokenOut: str
    chainId: int

class SwapTokenToTokenDto(BaseModel):
    """Swap token to token request"""
    inputMint: str
    outputMint: str
    amount: float
    slippageBps: Optional[int] = None

class EvmSwapTokenToTokenDto(BaseModel):
    """Swap token to token request"""
    tokenIn: str
    tokenOut: str
    amount: str
    chainId: int

class SwapTokenToNativeDto(BaseModel):
    """Swap token to native request"""
    amount: str
    tokenIn: str
    chainId: int

class SwapSolToTokenDto(BaseModel):
    """Swap SOL to token request"""
    outputMint: str
    amount: float
    slippageBps: Optional[int] = None

class SwapTokenToSolDto(BaseModel):
    """Swap SOL to token request"""
    inputMint: str
    amount: float

class TokenDto(BaseModel):
    """Token information"""
    address: str
    symbol: str
    decimals: int

class SwapPriceDto(BaseModel):
    """0x swap quote response"""
    quoteId: str
    fromToken: TokenDto
    toToken: TokenDto
    fromAmount: str
    toAmount: str
    rate: str
    reverseRate: str
    minToAmount: str
    protocolFee: str
    protocolFeeToken: TokenDto
    estimatedGas: str
    priceImpact: str
    liquidityAvailable: bool
    expiryTimestamp: int  # Unix timestamp
    blockNumber: str
    chainId: int

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

    



class SwapDto(BaseModel):
    """Swap response"""
    signature: str
    txUrl: str

class TxHashDto(BaseModel):
    """Transaction hash"""
    txHash: str

class SwapPriceResponseDto(BaseModel):
    """Price response"""
    statusCode: int
    message: str
    data: SwapPriceDto
    errors: Optional[Dict[str, Any]] = None
    

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)
    


class TxHashResponseDto(BaseModel):
    
    statusCode: int
    message: str
    data: TxHashDto
    errors: Optional[Dict[str, Any]] = None
    

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)




class TxHashDto(BaseModel):

    txHash: str
    

class SwapQuoteResponseDto(BaseModel):
    statusCode: int
    message: str
    data: SwapQuoteDto
    errors: Optional[Dict[str, Any]] = None    

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)
    

    

class SwapQuoteDto(BaseModel):
    quoteId: str
    swapMode: str  # 'ExactIn' or 'ExactOut'
    froTtoken: SwapTokenInfoDto
    toToken: SwapTokenInfoDto
    amounts: SwapAmountsDto
    rates: SwapRatesDto
    fees: SwapFeesDto
    route: SwapRouteDto
    priceImpact: str
    usdValues: UsdValuesDto
    slippageTolerance: str
    expiryTimestamp: int
    expiresIn: int
    estimatedSwapTime: int
    network: str
    executable: bool
    warnings: List[str] 

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key) 
             
class SwapTokenInfoDto(BaseModel):
    address: str
    symbol: str
    name: str
    decimals: int


class SwapAmountsDto(BaseModel):
    inputAmount: str
    outputAmount: str
    minOutputAmount: str
    inputAmountRaw: str
    outputAmountRaw: str

class SwapRatesDto(BaseModel):
    rate: str
    reverseRate: str


class SwapFeesDto(BaseModel):
    protocolFeePercent: str
    protocolFeeAmount: str
    totalFeePercent: str
    totalFeeAmount: str
    gasFee: str
    totalCost: str

class SwapRouteDto(BaseModel):
    hops: int
    dexes: List[str]
    tokens: List[str]
    efficiencyScore: int

class UsdValuesDto(BaseModel):
    inputValue: float
    outputValue: float
    netValue: float


class SwapResponseDto(BaseModel):
    status_code: int
    message: str
    data: SwapDto
    errors: Optional[Any] = None


class SwapDto(BaseModel):
    signature: str
    txUrl: str

