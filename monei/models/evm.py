"""EVM wallet models"""

from typing import Optional, List,Any,Dict
from .base import BaseModel

class BalanceDto(BaseModel):
    """Balance model"""
    balance: str

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

class BalanceResponseDto(BaseModel):
    statusCode: int
    message: str
    data: BalanceDto
    errors:  Optional[Dict[str, Any]] = None

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)
    
class UserEvmPortfolioResponseDto(BaseModel):
    statusCode: int
    data: UserEvmPortfolioDto
    message: str
    errors:  Optional[Dict[str, Any]] = None

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

class UserTokenBalanceDto(BaseModel):
    """Token balance model"""
    contractAddress: Optional[str] = None
    name: str
    symbol: str
    decimals: int
    logoUrl: Optional[str] = None
    type: str  # "native" or "token"
    balance: str
    balanceUSD: str
    priceUSD: str
    rawBalance: str
    network: str

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

class UserEvmPortfolioDto(BaseModel):
    """EVM portfolio model"""
    userId: str
    walletAddress: str
    network: str
    totalPortfolioValueUSD: str
    nativeToken: Optional[UserTokenBalanceDto] = None
    tokens: List[UserTokenBalanceDto]
    updatedAt: str

    
    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

class SendNativeTokenDto(BaseModel):
    """Send native token request"""
    to: str
    amount: str
    chainId: int

class SendTokenDto(BaseModel):
    """Send ERC20 token request"""
    to: str
    tokenAddress: str
    amount: str
    chainId: int

class SupportedChainsResponseDto(BaseModel):
    statusCode: int
    message: str
    data: List[SupportedChainDto]
    errors:  Optional[Dict[str, Any]] = None
    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

class SupportedChainDto(BaseModel):
    chain_id: int
    name: str
    native_token: str
    block_explorer_url: str
    is_testnet: bool

class SendNativeTokenResponseDto(BaseModel):
    statusCode: int
    message: str
    data: Response
    errors:  Optional[Dict[str, Any]] = None
    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

class Response(BaseModel):
    txHash: str

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

class SendTokenResponseDto(BaseModel):
    statusCode: int
    message: str
    data: Response
    errors:  Optional[Dict[str, Any]] = None
    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

