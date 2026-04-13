"""Solana wallet models"""
from typing import Optional, Dict, Any, List 
from enum import Enum
from .base import BaseModel

class SolanaNetwork(str, Enum):
    MAINNET_BETA = "mainnet-beta"
    DEVNET = "devnet"
    TESTNET = "testnet"

class BalanceDto(BaseModel):
    """Balance model"""
    balance: str

class AddressDto(BaseModel):
    """Wallet address"""
    address: str

class WalletAddressResponseDto(BaseModel):
    statusCode: int
    message: str
    data: AddressDto
    errors:  Optional[Dict[str, Any]] = None
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


class TokenInfoDto(BaseModel):
    """Token information"""
    mintAddress: str
    name: str
    symbol: str
    balance: float
    rawBalance: str
    decimals: int
    priceUsd: Optional[float] = None
    valueUsd: Optional[float] = None

    

class PortfolioDto(BaseModel):
    """Solana portfolio"""
    userId: str
    address: str
    nativeBalance: str
    nativeBalanceLamports: str
    nativeBalanceUsd: Optional[float] = None
    tokens: List[TokenInfoDto]
    totalValueUsd: Optional[float] = None

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)

class PortfolioResponseDto(BaseModel):
    """Portfolio response wrapper"""
    statusCode: int
    message: str
    data: PortfolioDto
    errors: Optional[Dict[str, Any]] = None

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)


class TransferSolDto(BaseModel):
    """Transfer SOL request"""
    to: str
    amount: str
    network: Optional[SolanaNetwork] = SolanaNetwork.MAINNET_BETA

class TransferTokenDto(BaseModel):
    """Transfer SPL token request"""
    to: str
    tokenMintAddress: str
    amount: str
    network: Optional[SolanaNetwork] = SolanaNetwork.MAINNET_BETA

class SignatureDto(BaseModel):
    """Transaction signature"""
    signature: str

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)
    
class SignatureResponseDto(BaseModel):
    """Transaction Response"""
    statusCode: int
    message: str
    data: SignatureDto
    errors:  Optional[Dict[str, Any]] = None

    def __contains__(self, key):
        """Allow 'in' operator to work with attributes"""
        return hasattr(self, key)